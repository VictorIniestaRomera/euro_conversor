import math;
import tkinter as tk;

from xmlreader import XMLReader;
from scrapper import Scrapper;
from coinconversor import CoinConversor;

def main():
    Scrapper().scrap();

    currency_list = XMLReader().read();

    background = "#f1f5f2";
    app = tk.Tk();
    app.title("Euro Converter");
    app.geometry("480x500");
    app.configure(bg=background);

    currencies = tuple(currency_list.keys());

    from_currency = tk.StringVar(value=currencies[0]);
    to_currency = tk.StringVar(value=currencies[1]);

    page = tk.Frame(app, bg=background, padx=28, pady=24);
    page.pack(fill="both", expand=True);

    tk.Label(page, text="Euro Converter", bg=background, fg="#203c35", font=("Segoe UI", 22, "bold")).pack(anchor="w");

    tk.Label(page, text="Select the currencies you want to convert between.", bg=background, fg="#687a73", font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 18));

    card = tk.Frame(page, bg="white", padx=20, pady=20);
    card.pack(fill="x");

    amount = tk.StringVar(value="1");
    amount_selector = tk.Frame(card, bg="white");
    amount_selector.pack(fill="x", pady=(0, 16));

    tk.Label(amount_selector, text="AMOUNT", bg="white", fg="#52665e", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 6));

    amount_entry = tk.Entry(
        amount_selector,
        textvariable=amount,
        bg="#f7faf8",
        fg="#203c35",
        relief="flat",
        highlightthickness=1,
        highlightbackground="#dce5df",
        font=("Segoe UI", 10)
    );
    amount_entry.pack(fill="x", ipady=8);

    choices = tk.Frame(card, bg="white");
    choices.pack(fill="x");
    choices.columnconfigure(0, weight=1);
    choices.columnconfigure(1, weight=1);

    for column, label, currency in ((0, "FROM", from_currency), (1, "TO", to_currency)):
        selector = tk.Frame(choices, bg="white");
        selector.grid(row=0, column=column, sticky="ew", padx=(0, 8) if column == 0 else (8, 0));

        tk.Label(selector, text=label, bg="white", fg="#52665e", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 6));

        menu_button = tk.OptionMenu(selector, currency, *currencies);
        menu_button.configure(
            bg="#f7faf8",
            fg="#203c35",
            activebackground="#e5eee8",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#dce5df",
            font=("Segoe UI", 10),
            padx=8,
            pady=6
        );
        menu_button["menu"].configure(font=("Segoe UI", 10));
        menu_button.pack(fill="x");

    result_box = tk.Frame(card, bg="#edf5f0", padx=14, pady=12);
    result_box.pack(fill="x", pady=(20, 14));

    tk.Label(result_box, text="RESULT", bg="#edf5f0", fg="#687a73", font=("Segoe UI", 9, "bold")).pack(anchor="w");

    result_label = tk.Label(result_box, text="Your result will appear here", bg="#edf5f0", fg="#176b55", font=("Segoe UI", 12, "bold"));
    result_label.pack(anchor="w", pady=(5, 0));

    coin_conversor = CoinConversor(currency_list);

    def convert_selected() -> None:
        try:
            quantity = float(amount.get());
        except ValueError:
            result_label.configure(text="Enter a valid amount (0 or greater).", fg="#b42318");

            return;
    
        if not math.isfinite(quantity) or quantity < 0:
            result_label.configure(text="Enter a valid amount (0 or greater).", fg="#b42318");
            
            return;

        source = from_currency.get();
        target = to_currency.get();
        result = coin_conversor.convert(quantity, source, target);
        result_label.configure(text=f"{quantity:g} {source} = {result:.4f} {target}", fg="#176b55");

    tk.Button(
        card,
        text="Convert",
        bg="#176b55",
        fg="white",
        activebackground="#125541",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2",
        pady=9,
        command=convert_selected
    ).pack(fill="x");

    app.mainloop();

if __name__ == "__main__":
    main();