public class Mitglied {
  // Deklaration der Objektvariablen
  private String name;
  private int alter;
  private int minKm;
  private int maxKm;

  // Deklaration des Konstruktors
  public Mitglied(String name, int alter) {
    this.name = name;
    this.alter = alter;
  }

  // Deklaration der Methoden
  public void nameSetzen(String name) {
    this.name = name;
  }

  public void alterSetzen(int alter) {
    this.alter = alter;
  }

  public void minKmSetzen(int minKm) {
    this.minKm = minKm;
  }

  public void maxKmSetzen(int maxKm) {
    this.maxKm = maxKm;
  }

  public String nameGeben() {
    return name;
  }

  public int alterGeben() {
    return alter;
  }

  public int minKmGeben() {
    return minKm;
  }

  public int maxKmGeben() {
    return maxKm;
  }
}
