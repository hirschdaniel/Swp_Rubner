
abstract class Pizzeria { 
	public void backen() {
		System.out.println("backen");
	} 
	public void schneiden() {
		System.out.println("schneiden");
	} 
	public void einpacken() {
		System.out.println("einpacken");
	}
	public abstract String stadt();
	public abstract String zutaten();
	//Salami, Hawaii, Calzone, Quattro Stagioni)

	public Pizzeria(String zutaten) {
		String temp ="";
		if(this.zutaten().equals("Salami")) {
			temp = "Diavolo"+this.stadt();
			backen();
			schneiden();
			einpacken();
			System.out.println(temp);
		}else if(this.zutaten().equals("Annanas")) {
			temp = "Hawai"+this.stadt();
			backen();
			schneiden();
			einpacken();
			System.out.println(temp);
		}else if(this.zutaten().equals("Gefalten")) {
			temp = "Calzone"+this.stadt();
			backen();
			schneiden();
			einpacken();
			System.out.println(temp);
		}else if(this.zutaten().equalsIgnoreCase("Kaese")) {
			temp = "Quattro Stagioni"+this.stadt();
			backen();
			schneiden();
			einpacken();
			System.out.println(temp);
		}else {
			temp = "Fehler";
			System.out.println(temp);
		}
	}
}







