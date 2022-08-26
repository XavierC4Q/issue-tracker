import React from "react";

interface IFooter {
  isLoggedIn: boolean;
}

export const Footer: React.FC<IFooter> = ({ isLoggedIn }) => {
  return (
    <footer>
      <h6>Footer tehe</h6>
    </footer>
  );
};
