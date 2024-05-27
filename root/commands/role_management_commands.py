# File: root/commands/role_management_commands.py (Python)

# Import necessary packages
import discord
from discord.ext import commands

# Define RoleManagementCommands class for role management functionalities
class RoleManagementCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to assign a role to a member
    @commands.command(name='assign_role')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been assigned the {role.name} role.')
        except Exception as e:
            await ctx.send(f'Error assigning role: {e}')

    # Command to remove a role from a member
    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f'{role.name} role has been removed from {member.mention}.')
        except Exception as e:
            await ctx.send(f'Error removing role: {e}')

    # Command to create a new role
    @commands.command(name='create_role')
    async def create_role(self, ctx, role_name):
        try:
            guild = ctx.guild
            await guild.create_role(name=role_name)
            await ctx.send(f'Role {role_name} has been created.')
        except Exception as e:
            await ctx.send(f'Error creating role: {e}')

# Setup function to add the RoleManagementCommands cog to the bot
def setup(bot):
    bot.add_cog(RoleManagementCommands(bot))