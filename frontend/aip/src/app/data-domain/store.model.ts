export interface StoreFilter{
    [key: string]: string | number | string[] | number[]
}

export interface StoreState{
    filter: StoreFilter
}