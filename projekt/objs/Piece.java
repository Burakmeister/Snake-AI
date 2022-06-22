package objs;

import java.awt.Rectangle;
import java.awt.Color;

public class Piece extends Rectangle {
    public static final int SIZE = 50;
    public static final Color COLOR = Color.WHITE;
    public Piece prevPosition;

    public Piece() {
        super.height = Piece.SIZE;
        super.width = Piece.SIZE;
        super.x = 0;
        super.y = 0;
    }

    public Piece(int x, int y) {
        super.height = Piece.SIZE;
        super.width = Piece.SIZE;
        super.x = x;
        super.y = y;
    }
}
