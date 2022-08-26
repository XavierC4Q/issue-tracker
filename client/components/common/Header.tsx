interface IHeader {
  isLoggedIn: boolean;
}

export const Header: React.FC<IHeader> = ({ isLoggedIn }) => {
  return (
    <header>
      <h1>Issue Tracker</h1>
    </header>
  );
};
