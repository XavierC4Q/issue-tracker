export interface UserNode {
  uid: string;
  email: string;
}

export interface Profile {
  fullname: string;
  profileId: string;
  title: string;
}

export interface UserType extends UserNode {
  profile: Profile | null;
}

export interface IMeQuery {
  me: UserNode | null;
}

export interface ITokenAuthMutation {
  tokenAuth: {
    token: string;
    success: boolean;
    errors: { [key: string]: any };
  };
}
