<script lang="ts">
	import NavButton from "./NavButton.svelte";
	import { goto } from "$app/navigation";

	import "../app.scss";

	let { children } = $props();

	const logout = async () => {
		await fetch("/auth/api/logout", {
			method: "POST",
			body: JSON.stringify({ targetURL: "/auth" }),
			headers: {
				"Content-Type": "application/json"
			}
		});
		await goto("/auth");
	};
</script>

<svelte:head>
	<title>Admin | ClayenApps Workspaces</title>
</svelte:head>

<div id="wrapper">
	<nav>
		<NavButton href="/" icon="/icons/home.svg" tooltip="Главная" />
		<NavButton href="/users" icon="/icons/users.svg" tooltip="Пользователи" match="parent" />
		<NavButton href="/monitor" icon="/icons/monitor.svg" tooltip="Мониторинг" match="parent" />
		<NavButton href="/db" icon="/icons/database.svg" tooltip="База данных" match="parent" />
		<div style:margin="auto 0"></div>
		<NavButton onclick={logout} icon="/icons/logout.svg" tooltip="Выход" />
	</nav>
	<main>{@render children()}</main>
</div>

<style lang="scss">
	#wrapper {
		display: flex;
		height: 100dvh;
	}
	nav {
		flex: 0 1 content;
		display: flex;
		flex-direction: column;
		background-color: var(--sidebar);
	}
	main {
		flex: 1;
		display: flex;
		flex-direction: column;
	}
</style>
