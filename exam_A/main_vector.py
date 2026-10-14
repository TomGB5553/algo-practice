from src.vector import Vector2D


def main() -> None:
    v1=Vector2D(3,4)
    v2=Vector2D(-1,2)
    print(v1+v2)
    print(v1 if v2 < v1 else v2)
    
if __name__ == "__main__":
    main()