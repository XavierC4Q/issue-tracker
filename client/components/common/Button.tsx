interface IButton {
  children: any;
  type: "button" | "submit";
}

export const Button: React.FC<IButton> = ({ children, type }) => {
  return <button type={type}>{children}</button>;
};
