import pygame
import chess

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess")

board = chess.Board()

selected_square = None


def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color,
                             (col*SQUARE_SIZE, row*SQUARE_SIZE,
                              SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces():
    font = pygame.font.SysFont("Arial", 36)

    piece_symbols = {
        "P":"♙","R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔",
        "p":"♟","r":"♜","n":"♞","b":"♝","q":"♛","k":"♚"
    }

    for square in chess.SQUARES:
        piece = board.piece_at(square)

        if piece:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)

            text = font.render(piece_symbols[piece.symbol()], True, (0,0,0))
            screen.blit(text,
                        (col*SQUARE_SIZE+20, row*SQUARE_SIZE+20))


def main():
    global selected_square

    running = True

    while running:
        draw_board()
        draw_pieces()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                square = chess.square(col, 7-row)

                if selected_square is None:
                    selected_square = square
                else:
                    move = chess.Move(selected_square, square)

                    if move in board.legal_moves:
                        board.push(move)

                    selected_square = None

        pygame.display.flip()

    pygame.quit()


main()