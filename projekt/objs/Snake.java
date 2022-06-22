package objs;

import java.util.ArrayList;

public class Snake {

    private ArrayList<Piece> pieces;
    private int vector; // 1-w 2-a 3-s 4-d

    public Snake() {
        this.vector = 4;
        this.pieces = new ArrayList<>();
        this.pieces.add(new Piece());
        this.pieces.get(0).prevPosition = new Piece();
    }

    public ArrayList<Piece> getPieces() {
        return this.pieces;
    }

    public void setVector(int v) {
        this.vector = v;
    }

    public int getVector() {
        return this.vector;
    }

    public void addPiece() {
        this.pieces.add(new Piece(this.pieces.get(this.pieces.size() - 1).prevPosition.x,
                this.pieces.get(this.pieces.size() - 1).prevPosition.y));
        this.pieces.get(this.pieces.size() - 1).prevPosition = new Piece();
    }
}
