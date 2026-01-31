from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import psutil
import os
import datetime

TOKEN = "8258998252:AAF9IaSM7jA6bngy_vK7SAK8TEBfc6lyb88"


# ---------- COMMANDS ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 DevOps Monitoring Bot\n\n"
        "/status - Server status\n"
        "/cpu - CPU usage\n"
        "/ram - Memory usage\n"
        "/disk - Disk usage\n"
        "/logs - Last 50 logs"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Server is running smoothly")


async def cpu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usage = psutil.cpu_percent(interval=1)
    await update.message.reply_text(f"🧠 CPU Usage: {usage}%")


async def ram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    memory = psutil.virtual_memory()
    await update.message.reply_text(
        f"💾 RAM Usage:\n"
        f"Total: {memory.total // (1024**2)} MB\n"
        f"Used: {memory.used // (1024**2)} MB\n"
        f"Percent: {memory.percent}%"
    )


async def disk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    disk = psutil.disk_usage('/')
    await update.message.reply_text(
        f"📀 Disk Usage:\n"
        f"Total: {disk.total // (1024**3)} GB\n"
        f"Used: {disk.used // (1024**3)} GB\n"
        f"Percent: {disk.percent}%"
    )


async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_file = "/var/log/syslog"

    if not os.path.exists(log_file):
        await update.message.reply_text("❌ Logs not found (Windows system)")
        return

    with open(log_file, "r") as file:
        last_logs = file.readlines()[-50:]

    await update.message.reply_text("📄 Last 50 Logs:\n" + "".join(last_logs))


# ---------- MAIN ----------

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("cpu", cpu))
app.add_handler(CommandHandler("ram", ram))
app.add_handler(CommandHandler("disk", disk))
app.add_handler(CommandHandler("logs", logs))

print("🤖 Bot is running...")
app.run_polling()
