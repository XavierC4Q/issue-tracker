import getTestIDs from '../../utils/getTestIds';

interface IButton {
  children: any;
  type?: 'button' | 'submit';
}

export const buttonTestIds: ReturnType<typeof getTestIDs> & {
  button?: string;
} = getTestIDs();

export const Button: React.FC<IButton> = ({ children, type = 'button' }) => {
  return (
    <button data-testid={buttonTestIds.button} type={type}>
      {children}
    </button>
  );
};
