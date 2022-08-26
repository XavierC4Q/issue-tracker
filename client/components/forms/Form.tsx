import { Button } from "../common/Button";

interface IForm {
  children: React.ReactNode | React.ReactNode[];
  handleSubmit: (event: React.FormEvent<HTMLFormElement>) => void;
}

export const Form: React.FC<IForm> = ({ children, handleSubmit }) => {
  return (
    <form onSubmit={handleSubmit}>
      {children}
      <Button type="submit">Submit</Button>
    </form>
  );
};
