package objs;

import java.awt.Rectangle;
import java.util.Random;
import java.awt.Color;

public class Apple extends Rectangle {
    public static final int SIZE = 50;
    public static final Color COLOR = Color.RED;
    private Random random;
    private final int MAX_X = 12, MAX_Y = 16;

    public Apple() {
        this.random = new Random();
        super.height = Piece.SIZE;
        super.width = Piece.SIZE;
        super.x = (this.random.nextInt(this.MAX_X - 1) + 1) * SIZE;
        super.y = (this.random.nextInt(this.MAX_Y - 1) + 1) * SIZE;
    }

    public void newApple() {
        super.x = this.random.nextInt(this.MAX_X) * SIZE;
        super.y = this.random.nextInt(this.MAX_Y) * SIZE;
    }
}