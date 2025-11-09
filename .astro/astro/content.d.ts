declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"members": {
"student-zhang.md": {
	id: "student-zhang.md";
  slug: "student-zhang";
  body: string;
  collection: "members";
  data: InferEntrySchema<"members">
} & { render(): Render[".md"] };
"teacher-wang.md": {
	id: "teacher-wang.md";
  slug: "teacher-wang";
  body: string;
  collection: "members";
  data: InferEntrySchema<"members">
} & { render(): Render[".md"] };
"李文涛.md": {
	id: "李文涛.md";
  slug: "李文涛";
  body: string;
  collection: "members";
  data: InferEntrySchema<"members">
} & { render(): Render[".md"] };
};
"news": {
"2023-12-10-neurips.md": {
	id: "2023-12-10-neurips.md";
  slug: "2023-12-10-neurips";
  body: string;
  collection: "news";
  data: InferEntrySchema<"news">
} & { render(): Render[".md"] };
};
"publications": {
"award-2018.md": {
	id: "award-2018.md";
  slug: "award-2018";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"award-2019.md": {
	id: "award-2019.md";
  slug: "award-2019";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"award-2021.md": {
	id: "award-2021.md";
  slug: "award-2021";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"award-students.md": {
	id: "award-students.md";
  slug: "award-students";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"book-1.md": {
	id: "book-1.md";
  slug: "book-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"book-2.md": {
	id: "book-2.md";
  slug: "book-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"book-3.md": {
	id: "book-3.md";
  slug: "book-3";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"book-4.md": {
	id: "book-4.md";
  slug: "book-4";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"book-5.md": {
	id: "book-5.md";
  slug: "book-5";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2013.md": {
	id: "paper-2013.md";
  slug: "paper-2013";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2014.md": {
	id: "paper-2014.md";
  slug: "paper-2014";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2016-1.md": {
	id: "paper-2016-1.md";
  slug: "paper-2016-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2016-2.md": {
	id: "paper-2016-2.md";
  slug: "paper-2016-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2017-1.md": {
	id: "paper-2017-1.md";
  slug: "paper-2017-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2018.md": {
	id: "paper-2018.md";
  slug: "paper-2018";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2019.md": {
	id: "paper-2019.md";
  slug: "paper-2019";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2023-1.md": {
	id: "paper-2023-1.md";
  slug: "paper-2023-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2023-2.md": {
	id: "paper-2023-2.md";
  slug: "paper-2023-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"paper-2024.md": {
	id: "paper-2024.md";
  slug: "paper-2024";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2017-1.md": {
	id: "patent-2017-1.md";
  slug: "patent-2017-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2017-2.md": {
	id: "patent-2017-2.md";
  slug: "patent-2017-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2018-1.md": {
	id: "patent-2018-1.md";
  slug: "patent-2018-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2019-1.md": {
	id: "patent-2019-1.md";
  slug: "patent-2019-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2021-1.md": {
	id: "patent-2021-1.md";
  slug: "patent-2021-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2021-2.md": {
	id: "patent-2021-2.md";
  slug: "patent-2021-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2023-1.md": {
	id: "patent-2023-1.md";
  slug: "patent-2023-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2024-1.md": {
	id: "patent-2024-1.md";
  slug: "patent-2024-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"patent-2024-2.md": {
	id: "patent-2024-2.md";
  slug: "patent-2024-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-2021-1.md": {
	id: "project-2021-1.md";
  slug: "project-2021-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-2022-1.md": {
	id: "project-2022-1.md";
  slug: "project-2022-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-2024-u35.md": {
	id: "project-2024-u35.md";
  slug: "project-2024-u35";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-participate-2016.md": {
	id: "project-participate-2016.md";
  slug: "project-participate-2016";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-participate-2018-1.md": {
	id: "project-participate-2018-1.md";
  slug: "project-participate-2018-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-participate-2018-2.md": {
	id: "project-participate-2018-2.md";
  slug: "project-participate-2018-2";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-participate-2020-1.md": {
	id: "project-participate-2020-1.md";
  slug: "project-participate-2020-1";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
"project-participate-2024-major.md": {
	id: "project-participate-2024-major.md";
  slug: "project-participate-2024-major";
  body: string;
  collection: "publications";
  data: InferEntrySchema<"publications">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = typeof import("./../../src/content/config.js");
}
