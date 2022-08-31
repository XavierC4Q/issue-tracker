import { Footer, footerTestIds } from '../../components/common/Footer';
import { render, screen } from '@testing-library/react';

describe('Footer Component', () => {
  it('renders the Footer', () => {
    render(<Footer isLoggedIn />);

    screen.getByTestId(footerTestIds.footer as string);
  });
});
