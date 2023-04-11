public class Berlin extends Pizzeria{

	private String zutaten;

	public Berlin(String zutaten) {
		super(zutaten);
	}

	@Override
	public String stadt() {
		String temp = "Berlin";
		return temp;
	}

	@Override
	public String zutaten() {
		return this.zutaten;
	}
}
