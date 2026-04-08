from dataclasses import dataclass
import pygame


@dataclass
class PlayingCard():
    damage: int
    reinforcement: int
    element:str
    special:str
    
    def __str__(self):
        return f"Damage: {self.damage}, Reinforcement: {self.reinforcement}, Element: {self.element}, Special: {self.special}"

    
    def draw(self, surface, x, y):
        # Draw the card background
        pygame.draw.rect(surface, (255, 255, 255), (x, y, 100, 150))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, 100, 150), 2)

        # Draw the card details
        font = pygame.font.SysFont(None, 24)
        damage_text = font.render(f"Damage: {self.damage}", True, (0, 0, 0))
        reinforcement_text = font.render(f"Reinforcement: {self.reinforcement}", True, (0, 0, 0))
        element_text = font.render(f"Element: {self.element}", True, (0, 0, 0))
        special_text = font.render(f"Special: {self.special}", True, (0, 0, 0))

        surface.blit(damage_text, (x + 10, y + 10))
        surface.blit(reinforcement_text, (x + 10, y + 40))
        surface.blit(element_text, (x + 10, y + 70))
        surface.blit(special_text, (x + 10, y + 100))
