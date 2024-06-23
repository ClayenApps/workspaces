<script lang="ts">
	import { page } from "$app/stores";

	let { icon, tooltip, ...props }: (LinkProps | ButtonProps) & CommonProps = $props();

	type CommonProps = { icon: string; tooltip?: string };
	type LinkProps = { href: string; match?: "exact" | "parent" };
	type ButtonProps = { onclick: () => void };

	function selected({ match = "exact", href }: LinkProps) {
		if (match === "exact") {
			return href === $page.url.pathname;
		} else {
			return $page.url.pathname.includes(href);
		}
	}
</script>

{#if "href" in props}
	<a href={props.href} title={tooltip} class:selected={selected(props)}>
		<img src={icon} alt={tooltip ?? ""} />
	</a>
{:else}
	<button onclick={props.onclick} title={tooltip}>
		<img src={icon} alt={tooltip ?? ""} />
	</button>
{/if}

<style lang="scss">
	a,
	button {
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: var(--sidebar);
		border: 0;
		width: 40px;
		height: 40px;
		cursor: pointer;
		&:hover {
			background-color: var(--sidebar-hover);
		}
		&.selected {
			cursor: default;
			background-color: var(--sidebar-selected);
		}
		> img {
			filter: invert(1);
			width: 24px;
			height: 24px;
		}
	}
</style>
