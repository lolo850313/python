package runnoob.collection;

import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;

public class addAndSizeOfCollection_4 {
    public static void main(String[] args) throws IOException {
        System.out.println("集合实例！\n");
        int size;
        HashSet collection = new HashSet();
        String str1 = "Yellow", str2 = "White", str3 = "Green", str4 = "Blue";
        Iterator iterator;
        collection.add(str1);
        collection.add(str2);
        collection.add(str3);
        collection.add(str4);
        System.out.println("集合数据： ");
        iterator = collection.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next() + " ");
        }
        System.out.println();
        size = collection.size();
        if (collection.isEmpty()) {
            System.out.println("集合是空的");
        } else {
            System.out.println("集合长度" + size);
        }
        System.out.println();
    }
}
