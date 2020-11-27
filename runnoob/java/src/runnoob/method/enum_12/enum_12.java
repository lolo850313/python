package runnoob.method.enum_12;

enum Car{
    lamborghini(900),tata(2),audi(50),fiat(15),honda(12);
    private int price;
    Car(int p){
        price = p;
    }
    int getPrice(){
        return price;
    }
}
public class enum_12 {
    public static void main(String[] args) {
        System.out.println("所有汽车的价格：");
        for (Car c:Car.values()
             ) {
            System.out.println(c + " 需要" + c.getPrice() + " 千美元");
        }
    }
}
