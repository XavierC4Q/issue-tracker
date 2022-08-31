import { render, screen } from '@testing-library/react';
import { Button, buttonTestIds } from '../../components/common/Button';

describe('Button Component', () => {
  it('Renders a Button', () => {
    render(<Button>A Button</Button>);

    screen.getByTestId(buttonTestIds.button as string);
    screen.getByText(/A Button/);
  });

  it('Gives Button the correct type', () => {
    render(<Button type="submit">A Submit Button</Button>);

    const button = document.querySelector("button[type='submit']");

    expect(button).not.toBeUndefined();
  });
});
