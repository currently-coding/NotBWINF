public class Wandertag {
  // Deklaration der Objektvariablen
  private Mitglied[] member;
  private int laenge1;
  private int anzMemberLaenge1;
  private int laenge2;
  private int anzMemberLaenge2;
  private int laenge3;
  private int zaehler;
  private int[] anzProLaenge1;
  private int[] anzProLaenge2;
  private int[] anzProLaenge3;
  private Mitglied[] extra1;
  private Mitglied[] extra2;
  private int zaehlerExtra1;
  private int zaehlerExtra2;

  // Deklaration des Konstruktors
  public Wandertag(int anzMember, int laenge1, int laenge2, int laenge3) {
    this.member = new Mitglied[anzMember];
    anzProLaenge1 = new int[maxlaengeBerechnen()];
    anzProLaenge2 = new int[maxlaengeBerechnen()];
    anzProLaenge3 = new int[maxlaengeBerechnen()];
    this.laenge1 = laenge1;
    this.laenge2 = laenge2;
    this.laenge3 = laenge3;
    extra1 = new Mitglied[anzMember - anzMemberLaenge1];
    extra2 = new Mitglied[anzMember - anzMemberLaenge2];
  }

  // Deklaration der Methoden
  public void mitgliedHinzufuegen(Mitglied m) {
    if (zaehler < member.length) {
      member[zaehler] = m;
      zaehler++;
    }
  }

  public void extra1Hinzufuegen() {
    for (int i = 0; i < member.length; i++) {
      if ((member[i].minKmGeben() <= laenge1) && (member[i].maxKmGeben() >= laenge1)) {

      } else {
        extra1[zaehlerExtra1] = member[i];
        zaehlerExtra1++;
      }
    }
  }

  public void extra2Hinzufuegen() {
    for (int i = 0; i < extra1.length; i++) {
      if ((extra1[i].minKmGeben() <= laenge2) && (extra1[i].maxKmGeben() >= laenge2)) {

      } else {
        extra2[zaehlerExtra2] = extra1[i];
        zaehlerExtra2++;
      }
    }
  }

  public int maxlaengeBerechnen() {
    /*
     *
     *
     *
     *
    */
    int maxlaenge = 0;
    for (int i = 0; i < member.length; i++) {
      if (maxlaenge < member[i].maxKmGeben()) {
        maxlaenge = member[i].maxKmGeben();
      }
    }
    return maxlaenge;
  }

  public int laenge1Berechnen() {
    for (int i = 0; i < (maxlaengeBerechnen() + 1); i++) {
      for (int j = 0; j < member.length; j++) {
        if ((member[j].minKmGeben() <= i) && (member[j].maxKmGeben() >= i)) {
          anzProLaenge1[i]++;
        }
      }
    }

    for (int i = 0; i < anzProLaenge1.length; i++) {
      int max = 0;
      if (anzProLaenge1[i] > max) {
        max = anzProLaenge1[i];
        laenge1 = i;
      }
    }
    return laenge1;
  }

  public int laenge2Berechnen() {
    for (int i = 0; i < (maxlaengeBerechnen() + 1); i++) {
      for (int j = 0; j < extra1.length; j++) {
        if ((extra1[j].minKmGeben() <= i) && (extra1[j].maxKmGeben() >= i)) {
          anzProLaenge2[i]++;
        }
      }
    }
    for (int i = 0; i < anzProLaenge2.length; i++) {
      int max = 0;
      if (anzProLaenge2[i] > max) {
        max = anzProLaenge2[i];
        laenge2 = i;
      }
    }
    return laenge2;
  }

  public int laenge3Berechnen() {
    for (int i = 0; i < (maxlaengeBerechnen() + 1); i++) {
      for (int j = 0; j < extra2.length; j++) {
        if ((extra2[j].minKmGeben() <= i) && (extra2[j].maxKmGeben() >= i)) {
          anzProLaenge3[i]++;
        }
      }
    }
    for (int i = 0; i < anzProLaenge3.length; i++) {
      int max = 0;
      if (anzProLaenge3[i] > max) {
        max = anzProLaenge3[i];
        laenge3 = i;
      }
    }
    return laenge3;
  }

  public void laengenBerechnen() {
    laenge1Berechnen();
    laenge2Berechnen();
    laenge3Berechnen();
  }
}
