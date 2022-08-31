import React from 'react';
import getTestIDs from '../../utils/getTestIds';

interface IFooter {
  isLoggedIn: boolean;
}

export const footerTestIds: ReturnType<typeof getTestIDs> & {
  footer?: string;
} = getTestIDs();

export const Footer: React.FC<IFooter> = ({ isLoggedIn }) => {
  return (
    <footer data-testid={footerTestIds.footer}>
      <h6>Footer tehe</h6>
    </footer>
  );
};
