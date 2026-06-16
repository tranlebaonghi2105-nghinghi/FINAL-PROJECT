import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class GUIView:
    """Main GUI window for Cafe Management System."""

    def __init__(
        self,
        menu_service,
        table_service,
        promotion_service,
        invoice_service,
        on_exit
    ):
        self.menu_service = menu_service
        self.table_service = table_service
        self.promotion_service = promotion_service
        self.invoice_service = invoice_service
        self.on_exit = on_exit

        self.root = tk.Tk()
        self.root.title("Cafe Management System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f5f5f5")

        self._build_ui()

    # ------------------------------------------------------------------ #
    #  BUILD UI
    # ------------------------------------------------------------------ #

    def _build_ui(self):
        # Title bar
        title = tk.Label(
            self.root,
            text="☕  CAFE MANAGEMENT SYSTEM",
            font=("Helvetica", 18, "bold"),
            bg="#4a90d9",
            fg="white",
            pady=12
        )
        title.pack(fill=tk.X)

        # Notebook (tabs)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TNotebook.Tab",
            font=("Helvetica", 11, "bold"),
            padding=[12, 6]
        )

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Build each tab
        self._build_menu_tab()
        self._build_table_tab()
        self._build_promotion_tab()
        self._build_invoice_tab()
        self._build_statistics_tab()

        # Bind tab change để tự động load statistics
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

        # Exit button
        exit_btn = tk.Button(
            self.root,
            text="💾  Save & Exit",
            font=("Helvetica", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            command=self._exit
        )
        exit_btn.pack(pady=(0, 10))

    # ------------------------------------------------------------------ #
    #  HELPER: create a Treeview with scrollbar
    # ------------------------------------------------------------------ #

    def _make_tree(self, parent, columns):
        frame = tk.Frame(parent, bg="#f5f5f5")
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER, width=160)

        sb = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=sb.set)

        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        return tree

    def _make_button_row(self, parent, buttons):
        """buttons = list of (label, bg, command)"""
        row = tk.Frame(parent, bg="#f5f5f5")
        row.pack(pady=6)
        for label, bg, cmd in buttons:
            tk.Button(
                row,
                text=label,
                bg=bg,
                fg="white",
                font=("Helvetica", 10, "bold"),
                relief=tk.FLAT,
                padx=12,
                pady=6,
                command=cmd
            ).pack(side=tk.LEFT, padx=5)

    # ================================================================== #
    #  TAB 1: MENU
    # ================================================================== #

    def _build_menu_tab(self):
        tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(tab, text="🍽  Menu")

        self.menu_tree = self._make_tree(
            tab,
            ["ID", "Name", "Type", "Base Price", "Final Price"]
        )

        self._make_button_row(tab, [
            ("➕ Add",     "#27ae60", self._menu_add),
            ("✏️ Update",  "#f39c12", self._menu_update),
            ("🗑 Delete",  "#e74c3c", self._menu_delete),
            ("🔍 Search",  "#8e44ad", self._menu_search),
            ("🔃 Sort ↑",  "#2980b9", self._menu_sort_asc),
            ("🔃 Sort ↓",  "#2980b9", self._menu_sort_desc),
            ("🔄 Refresh", "#7f8c8d", self._menu_refresh),
        ])

        self._menu_refresh()

    def _menu_refresh(self, items=None):
        for row in self.menu_tree.get_children():
            self.menu_tree.delete(row)
        if items is None:
            items = self.menu_service.get_all_items()
        for item in items:
            type_name = self.menu_service.get_item_type(item)
            self.menu_tree.insert("", tk.END, values=(
                item.item_id,
                item.name,
                type_name,
                f"{item.price:.2f}",
                f"{item.calculate_price():.2f}"
            ))

    def _menu_add(self):
        item_type = simpledialog.askstring(
            "Add Item",
            "Item type (Food / Drink / Combo):"
        )
        if not item_type:
            return
        item_id = simpledialog.askstring("Add Item", "Item ID:")
        if not item_id:
            return
        name = simpledialog.askstring("Add Item", "Item name:")
        if not name:
            return
        price_str = simpledialog.askstring("Add Item", "Price:")
        try:
            price = float(price_str)
            self.menu_service.add_item(item_type, item_id, name, price)
            messagebox.showinfo("Success", "Item added successfully.")
            self._menu_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _menu_update(self):
        item_id = simpledialog.askstring("Update Item", "Item ID to update:")
        if not item_id:
            return
        price_str = simpledialog.askstring("Update Item", "New price:")
        try:
            new_price = float(price_str)
            self.menu_service.update_item(item_id, new_price)
            messagebox.showinfo("Success", "Updated successfully.")
            self._menu_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _menu_delete(self):
        selected = self.menu_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an item.")
            return
        item_id = self.menu_tree.item(selected[0])["values"][0]
        if messagebox.askyesno("Confirm", f"Delete item {item_id}?"):
            try:
                self.menu_service.delete_item(str(item_id))
                self._menu_refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _menu_search(self):
        keyword = simpledialog.askstring("Search", "Enter name keyword:")
        if keyword is not None:
            result = self.menu_service.search_by_name(keyword)
            self._menu_refresh(result)

    def _menu_sort_asc(self):
        self._menu_refresh(self.menu_service.sort_by_price_ascending())

    def _menu_sort_desc(self):
        self._menu_refresh(self.menu_service.sort_by_price_descending())

    # ================================================================== #
    #  TAB 2: TABLES
    # ================================================================== #

    def _build_table_tab(self):
        tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(tab, text="🪑  Tables")

        self.table_tree = self._make_tree(tab, ["Table ID", "Status"])

        self._make_button_row(tab, [
            ("➕ Add Table",     "#27ae60", self._table_add),
            ("✏️ Update Status", "#f39c12", self._table_update),
            ("🔄 Refresh",       "#7f8c8d", self._table_refresh),
        ])

        self._table_refresh()

    def _table_refresh(self):
        for row in self.table_tree.get_children():
            self.table_tree.delete(row)
        for table in self.table_service.get_all_tables():
            self.table_tree.insert(
                "", tk.END,
                values=(table.table_id, table.status)
            )

    def _table_add(self):
        table_id = simpledialog.askstring("Add Table", "Table ID:")
        if not table_id:
            return
        try:
            self.table_service.add_table(table_id)
            messagebox.showinfo("Success", "Table added.")
            self._table_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _table_update(self):
        selected = self.table_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a table.")
            return
        table_id = self.table_tree.item(selected[0])["values"][0]
        status = simpledialog.askstring(
            "Update Status",
            "New status (Available / Occupied):"
        )
        try:
            self.table_service.update_status(str(table_id), status)
            self._table_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ================================================================== #
    #  TAB 3: PROMOTIONS
    # ================================================================== #

    def _build_promotion_tab(self):
        tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(tab, text="🎁  Promotions")

        self.promo_tree = self._make_tree(
            tab,
            ["Promotion ID", "Name", "Discount (%)"]
        )

        self._make_button_row(tab, [
            ("➕ Add",    "#27ae60", self._promo_add),
            ("🗑 Delete", "#e74c3c", self._promo_delete),
            ("🔄 Refresh","#7f8c8d", self._promo_refresh),
        ])

        self._promo_refresh()

    def _promo_refresh(self):
        for row in self.promo_tree.get_children():
            self.promo_tree.delete(row)
        for p in self.promotion_service.get_all_promotions():
            self.promo_tree.insert(
                "", tk.END,
                values=(p.promotion_id, p.name, f"{p.discount_percent:.1f}")
            )

    def _promo_add(self):
        pid = simpledialog.askstring("Add Promotion", "Promotion ID:")
        if not pid:
            return
        name = simpledialog.askstring("Add Promotion", "Name:")
        if not name:
            return
        pct = simpledialog.askstring("Add Promotion", "Discount percent (0-100):")
        try:
            self.promotion_service.add_promotion(pid, name, float(pct))
            messagebox.showinfo("Success", "Promotion added.")
            self._promo_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _promo_delete(self):
        selected = self.promo_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a promotion.")
            return
        pid = self.promo_tree.item(selected[0])["values"][0]
        if messagebox.askyesno("Confirm", f"Delete promotion {pid}?"):
            try:
                self.promotion_service.delete_promotion(str(pid))
                self._promo_refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    # ================================================================== #
    #  TAB 4: INVOICES
    # ================================================================== #

    def _build_invoice_tab(self):
        tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(tab, text="🧾  Invoices")

        self.invoice_tree = self._make_tree(
            tab,
            ["Invoice ID", "Table ID", "Subtotal", "Discount", "Total", "Promotion"]
        )

        self._make_button_row(tab, [
            ("➕ New Invoice",      "#27ae60", self._invoice_create),
            ("🍽 Add Item",         "#f39c12", self._invoice_add_item),
            ("🎁 Apply Promotion",  "#8e44ad", self._invoice_apply_promo),
            ("📤 Export CSV",       "#2980b9", self._invoice_export),
            ("🔄 Refresh",          "#7f8c8d", self._invoice_refresh),
        ])

        self._invoice_refresh()

    def _invoice_refresh(self):
        for row in self.invoice_tree.get_children():
            self.invoice_tree.delete(row)
        for inv in self.invoice_service.get_all_invoices():
            promo_name = inv.promotion.name if inv.promotion else "None"
            self.invoice_tree.insert("", tk.END, values=(
                inv.invoice_id,
                inv.table_id,
                f"{inv.calculate_subtotal():.2f}",
                f"{inv.calculate_discount_amount():.2f}",
                f"{inv.calculate_total():.2f}",
                promo_name
            ))

    def _invoice_create(self):
        inv_id = simpledialog.askstring("New Invoice", "Invoice ID:")
        if not inv_id:
            return
        tbl_id = simpledialog.askstring("New Invoice", "Table ID:")
        if not tbl_id:
            return
        try:
            self.invoice_service.create_invoice(inv_id, tbl_id)
            self.table_service.update_status(tbl_id, "Occupied")
            messagebox.showinfo("Success", "Invoice created.")
            self._invoice_refresh()
            self._table_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _invoice_add_item(self):
        inv_id = simpledialog.askstring("Add Item to Invoice", "Invoice ID:")
        if not inv_id:
            return
        item_id = simpledialog.askstring("Add Item to Invoice", "Item ID:")
        if not item_id:
            return
        item = self.menu_service.find_by_id(item_id)
        if item is None:
            messagebox.showerror("Error", "Item not found.")
            return
        try:
            self.invoice_service.add_item_to_invoice(inv_id, item)
            messagebox.showinfo("Success", "Item added to invoice.")
            self._invoice_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _invoice_apply_promo(self):
        inv_id = simpledialog.askstring("Apply Promotion", "Invoice ID:")
        if not inv_id:
            return
        promo_id = simpledialog.askstring("Apply Promotion", "Promotion ID:")
        if not promo_id:
            return
        promo = self.promotion_service.find_by_id(promo_id)
        if promo is None:
            messagebox.showerror("Error", "Promotion not found.")
            return
        try:
            self.invoice_service.apply_promotion_to_invoice(inv_id, promo)
            messagebox.showinfo("Success", "Promotion applied.")
            self._invoice_refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _invoice_export(self):
        try:
            filename = self.invoice_service.export_to_csv()
            messagebox.showinfo("Exported", f"Saved to: {filename}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ================================================================== #
    #  TAB 5: STATISTICS
    # ================================================================== #

    def _build_statistics_tab(self):
        tab = tk.Frame(self.notebook, bg="#f5f5f5")
        self.notebook.add(tab, text="📊  Statistics")

        self.stats_text = tk.Text(
            tab,
            font=("Courier", 12),
            bg="#ffffff",
            fg="#2c3e50",
            relief=tk.FLAT,
            padx=12,
            pady=12,
            state=tk.DISABLED
        )
        self.stats_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=(8, 4))

        self._make_button_row(tab, [
            ("🔄 Refresh Statistics", "#2980b9", self._stats_load),
        ])

    def _on_tab_changed(self, event):
        # Tab Statistics là tab thứ 5 (index 4)
        selected = self.notebook.index(self.notebook.select())
        if selected == 4:
            self._stats_load()

    def _stats_load(self):
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete("1.0", tk.END)

        total_revenue = self.invoice_service.get_total_revenue()
        invoice_count = self.invoice_service.get_invoice_count()
        most_exp = self.invoice_service.get_most_expensive_item()
        stats = self.invoice_service.get_statistics_by_type()

        lines = [
            "=" * 45,
            "  CAFE MANAGEMENT — STATISTICS",
            "=" * 45,
            f"  Total Invoices   : {invoice_count}",
            f"  Total Revenue    : {total_revenue:.2f}",
            "-" * 45,
            "  REVENUE BY ITEM TYPE",
            "-" * 45,
        ]
        for item_type, data in stats.items():
            lines.append(
                f"  {item_type:<10} — Count: {data['count']:>4}  |  "
                f"Revenue: {data['revenue']:>10.2f}"
            )
        lines.append("-" * 45)
        if most_exp:
            lines.append(
                f"  Most Expensive   : {most_exp.name} "
                f"({most_exp.calculate_price():.2f})"
            )
        lines.append("=" * 45)

        self.stats_text.insert(tk.END, "\n".join(lines))
        self.stats_text.config(state=tk.DISABLED)

    # ------------------------------------------------------------------ #
    #  EXIT
    # ------------------------------------------------------------------ #

    def _exit(self):
        if messagebox.askyesno("Exit", "Save data and exit?"):
            self.on_exit()
            self.root.destroy()

    def run(self):
        self.root.mainloop()