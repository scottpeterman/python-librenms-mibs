# SNMP MIB module (WTI-MPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wti\WTI-MPC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:25 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wti = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3)
)
if mibBuilder.loadTexts:
    wti.setRevisions(
        ("2008-12-17 15:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WesternTelematic_ObjectIdentity = ObjectIdentity
westernTelematic = _WesternTelematic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634)
)
_SystemTables_ObjectIdentity = ObjectIdentity
systemTables = _SystemTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100)
)
_PlugTable_Object = MibTable
plugTable = _PlugTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200)
)
if mibBuilder.loadTexts:
    plugTable.setStatus("current")
_PlugEntry_Object = MibTableRow
plugEntry = _PlugEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1)
)
plugEntry.setIndexNames(
    (0, "WTI-MPC-MIB", "plugIndex"),
)
if mibBuilder.loadTexts:
    plugEntry.setStatus("current")


class _PlugIndex_Type(Integer32):
    """Custom type plugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_PlugIndex_Type.__name__ = "Integer32"
_PlugIndex_Object = MibTableColumn
plugIndex = _PlugIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 1),
    _PlugIndex_Type()
)
plugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plugIndex.setStatus("current")


class _PlugID_Type(DisplayString):
    """Custom type plugID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 11),
    )


_PlugID_Type.__name__ = "DisplayString"
_PlugID_Object = MibTableColumn
plugID = _PlugID_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 2),
    _PlugID_Type()
)
plugID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugID.setStatus("current")


class _PlugStatus_Type(Integer32):
    """Custom type plugStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PlugStatus_Type.__name__ = "Integer32"
_PlugStatus_Object = MibTableColumn
plugStatus = _PlugStatus_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 3),
    _PlugStatus_Type()
)
plugStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugStatus.setStatus("current")


class _PlugAction_Type(Integer32):
    """Custom type plugAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PlugAction_Type.__name__ = "Integer32"
_PlugAction_Object = MibTableColumn
plugAction = _PlugAction_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 4),
    _PlugAction_Type()
)
plugAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plugAction.setStatus("current")
_PlugName_Type = DisplayString
_PlugName_Object = MibTableColumn
plugName = _PlugName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 5),
    _PlugName_Type()
)
plugName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugName.setStatus("current")
_PlugGroupTable_Object = MibTable
plugGroupTable = _PlugGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 300)
)
if mibBuilder.loadTexts:
    plugGroupTable.setStatus("current")
_PlugGroupEntry_Object = MibTableRow
plugGroupEntry = _PlugGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1)
)
plugGroupEntry.setIndexNames(
    (0, "WTI-MPC-MIB", "plugGroupIndex"),
)
if mibBuilder.loadTexts:
    plugGroupEntry.setStatus("current")


class _PlugGroupIndex_Type(Integer32):
    """Custom type plugGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_PlugGroupIndex_Type.__name__ = "Integer32"
_PlugGroupIndex_Object = MibTableColumn
plugGroupIndex = _PlugGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 1),
    _PlugGroupIndex_Type()
)
plugGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plugGroupIndex.setStatus("current")


class _PlugGroupName_Type(DisplayString):
    """Custom type plugGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_PlugGroupName_Type.__name__ = "DisplayString"
_PlugGroupName_Object = MibTableColumn
plugGroupName = _PlugGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 2),
    _PlugGroupName_Type()
)
plugGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plugGroupName.setStatus("current")


class _PlugGroupAction_Type(Integer32):
    """Custom type plugGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PlugGroupAction_Type.__name__ = "Integer32"
_PlugGroupAction_Object = MibTableColumn
plugGroupAction = _PlugGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 3),
    _PlugGroupAction_Type()
)
plugGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plugGroupAction.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1)
)
userEntry.setIndexNames(
    (0, "WTI-MPC-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPasswd_Type(DisplayString):
    """Custom type userPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UserPasswd_Type.__name__ = "DisplayString"
_UserPasswd_Object = MibTableColumn
userPasswd = _UserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 3),
    _UserPasswd_Type()
)
userPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPasswd.setStatus("current")


class _UserAccessLevel_Type(Integer32):
    """Custom type userAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UserAccessLevel_Type.__name__ = "Integer32"
_UserAccessLevel_Object = MibTableColumn
userAccessLevel = _UserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 4),
    _UserAccessLevel_Type()
)
userAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAccessLevel.setStatus("current")


class _UserPortAccess_Type(DisplayString):
    """Custom type userPortAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_UserPortAccess_Type.__name__ = "DisplayString"
_UserPortAccess_Object = MibTableColumn
userPortAccess = _UserPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 5),
    _UserPortAccess_Type()
)
userPortAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPortAccess.setStatus("current")


class _UserLocalAccess_Type(DisplayString):
    """Custom type userLocalAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UserLocalAccess_Type.__name__ = "DisplayString"
_UserLocalAccess_Object = MibTableColumn
userLocalAccess = _UserLocalAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 6),
    _UserLocalAccess_Type()
)
userLocalAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLocalAccess.setStatus("current")


class _UserAux1Access_Type(DisplayString):
    """Custom type userAux1Access based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UserAux1Access_Type.__name__ = "DisplayString"
_UserAux1Access_Object = MibTableColumn
userAux1Access = _UserAux1Access_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 7),
    _UserAux1Access_Type()
)
userAux1Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAux1Access.setStatus("current")


class _UserAux2Access_Type(DisplayString):
    """Custom type userAux2Access based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UserAux2Access_Type.__name__ = "DisplayString"
_UserAux2Access_Object = MibTableColumn
userAux2Access = _UserAux2Access_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 8),
    _UserAux2Access_Type()
)
userAux2Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAux2Access.setStatus("current")


class _UserAux3Access_Type(DisplayString):
    """Custom type userAux3Access based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UserAux3Access_Type.__name__ = "DisplayString"
_UserAux3Access_Object = MibTableColumn
userAux3Access = _UserAux3Access_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 9),
    _UserAux3Access_Type()
)
userAux3Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAux3Access.setStatus("current")


class _UserGroupAccess_Type(DisplayString):
    """Custom type userGroupAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 54),
    )


_UserGroupAccess_Type.__name__ = "DisplayString"
_UserGroupAccess_Object = MibTableColumn
userGroupAccess = _UserGroupAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 10),
    _UserGroupAccess_Type()
)
userGroupAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupAccess.setStatus("current")


class _UserSerialAccess_Type(Integer32):
    """Custom type userSerialAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserSerialAccess_Type.__name__ = "Integer32"
_UserSerialAccess_Object = MibTableColumn
userSerialAccess = _UserSerialAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 11),
    _UserSerialAccess_Type()
)
userSerialAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSerialAccess.setStatus("current")


class _UserTelnetSshAccess_Type(Integer32):
    """Custom type userTelnetSshAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserTelnetSshAccess_Type.__name__ = "Integer32"
_UserTelnetSshAccess_Object = MibTableColumn
userTelnetSshAccess = _UserTelnetSshAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 12),
    _UserTelnetSshAccess_Type()
)
userTelnetSshAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userTelnetSshAccess.setStatus("current")


class _UserWebAccess_Type(Integer32):
    """Custom type userWebAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserWebAccess_Type.__name__ = "Integer32"
_UserWebAccess_Object = MibTableColumn
userWebAccess = _UserWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 13),
    _UserWebAccess_Type()
)
userWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userWebAccess.setStatus("current")


class _UserCurrentPowerMetering_Type(Integer32):
    """Custom type userCurrentPowerMetering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserCurrentPowerMetering_Type.__name__ = "Integer32"
_UserCurrentPowerMetering_Object = MibTableColumn
userCurrentPowerMetering = _UserCurrentPowerMetering_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 15),
    _UserCurrentPowerMetering_Type()
)
userCurrentPowerMetering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCurrentPowerMetering.setStatus("current")


class _UserCallbackNum_Type(DisplayString):
    """Custom type userCallbackNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserCallbackNum_Type.__name__ = "DisplayString"
_UserCallbackNum_Object = MibTableColumn
userCallbackNum = _UserCallbackNum_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 16),
    _UserCallbackNum_Type()
)
userCallbackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userCallbackNum.setStatus("current")


class _UserSubmit_Type(Integer32):
    """Custom type userSubmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserSubmit_Type.__name__ = "Integer32"
_UserSubmit_Object = MibTableColumn
userSubmit = _UserSubmit_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 31),
    _UserSubmit_Type()
)
userSubmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSubmit.setStatus("current")
_EnvironmentTables_ObjectIdentity = ObjectIdentity
environmentTables = _EnvironmentTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200)
)
_EnvironmentUnitTable_Object = MibTable
environmentUnitTable = _EnvironmentUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10)
)
if mibBuilder.loadTexts:
    environmentUnitTable.setStatus("current")
_EnvironmentUnitEntry_Object = MibTableRow
environmentUnitEntry = _EnvironmentUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1)
)
environmentUnitEntry.setIndexNames(
    (0, "WTI-MPC-MIB", "environmentUnitIndex"),
)
if mibBuilder.loadTexts:
    environmentUnitEntry.setStatus("current")


class _EnvironmentUnitIndex_Type(Integer32):
    """Custom type environmentUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_EnvironmentUnitIndex_Type.__name__ = "Integer32"
_EnvironmentUnitIndex_Object = MibTableColumn
environmentUnitIndex = _EnvironmentUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 1),
    _EnvironmentUnitIndex_Type()
)
environmentUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    environmentUnitIndex.setStatus("current")


class _EnvironmentUnitName_Type(DisplayString):
    """Custom type environmentUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EnvironmentUnitName_Type.__name__ = "DisplayString"
_EnvironmentUnitName_Object = MibTableColumn
environmentUnitName = _EnvironmentUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 2),
    _EnvironmentUnitName_Type()
)
environmentUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitName.setStatus("current")
_EnvironmentUnitTemperature_Type = Integer32
_EnvironmentUnitTemperature_Object = MibTableColumn
environmentUnitTemperature = _EnvironmentUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 3),
    _EnvironmentUnitTemperature_Type()
)
environmentUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitTemperature.setStatus("current")
_EnvironmentUnitCurrentA_Type = Integer32
_EnvironmentUnitCurrentA_Object = MibTableColumn
environmentUnitCurrentA = _EnvironmentUnitCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 4),
    _EnvironmentUnitCurrentA_Type()
)
environmentUnitCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitCurrentA.setStatus("current")
_EnvironmentUnitVoltageA_Type = Integer32
_EnvironmentUnitVoltageA_Object = MibTableColumn
environmentUnitVoltageA = _EnvironmentUnitVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 5),
    _EnvironmentUnitVoltageA_Type()
)
environmentUnitVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitVoltageA.setStatus("current")
_EnvironmentUnitPowerA_Type = Integer32
_EnvironmentUnitPowerA_Object = MibTableColumn
environmentUnitPowerA = _EnvironmentUnitPowerA_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 6),
    _EnvironmentUnitPowerA_Type()
)
environmentUnitPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitPowerA.setStatus("current")
_EnvironmentUnitCurrentB_Type = Integer32
_EnvironmentUnitCurrentB_Object = MibTableColumn
environmentUnitCurrentB = _EnvironmentUnitCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 7),
    _EnvironmentUnitCurrentB_Type()
)
environmentUnitCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitCurrentB.setStatus("current")
_EnvironmentUnitVoltageB_Type = Integer32
_EnvironmentUnitVoltageB_Object = MibTableColumn
environmentUnitVoltageB = _EnvironmentUnitVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 8),
    _EnvironmentUnitVoltageB_Type()
)
environmentUnitVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitVoltageB.setStatus("current")
_EnvironmentUnitPowerB_Type = Integer32
_EnvironmentUnitPowerB_Object = MibTableColumn
environmentUnitPowerB = _EnvironmentUnitPowerB_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 9),
    _EnvironmentUnitPowerB_Type()
)
environmentUnitPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitPowerB.setStatus("current")
_EnvironmentUnitCurrentC_Type = Integer32
_EnvironmentUnitCurrentC_Object = MibTableColumn
environmentUnitCurrentC = _EnvironmentUnitCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 10),
    _EnvironmentUnitCurrentC_Type()
)
environmentUnitCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitCurrentC.setStatus("current")
_EnvironmentUnitVoltageC_Type = Integer32
_EnvironmentUnitVoltageC_Object = MibTableColumn
environmentUnitVoltageC = _EnvironmentUnitVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 11),
    _EnvironmentUnitVoltageC_Type()
)
environmentUnitVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitVoltageC.setStatus("current")
_EnvironmentUnitPowerC_Type = Integer32
_EnvironmentUnitPowerC_Object = MibTableColumn
environmentUnitPowerC = _EnvironmentUnitPowerC_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 12),
    _EnvironmentUnitPowerC_Type()
)
environmentUnitPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitPowerC.setStatus("current")
_EnvironmentUnitCurrentD_Type = Integer32
_EnvironmentUnitCurrentD_Object = MibTableColumn
environmentUnitCurrentD = _EnvironmentUnitCurrentD_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 13),
    _EnvironmentUnitCurrentD_Type()
)
environmentUnitCurrentD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitCurrentD.setStatus("current")
_EnvironmentUnitVoltageD_Type = Integer32
_EnvironmentUnitVoltageD_Object = MibTableColumn
environmentUnitVoltageD = _EnvironmentUnitVoltageD_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 14),
    _EnvironmentUnitVoltageD_Type()
)
environmentUnitVoltageD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitVoltageD.setStatus("current")
_EnvironmentUnitPowerD_Type = Integer32
_EnvironmentUnitPowerD_Object = MibTableColumn
environmentUnitPowerD = _EnvironmentUnitPowerD_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 15),
    _EnvironmentUnitPowerD_Type()
)
environmentUnitPowerD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentUnitPowerD.setStatus("current")
_EnvironmentBranchATotalCurrent_Type = Integer32
_EnvironmentBranchATotalCurrent_Object = MibScalar
environmentBranchATotalCurrent = _EnvironmentBranchATotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 20),
    _EnvironmentBranchATotalCurrent_Type()
)
environmentBranchATotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchATotalCurrent.setStatus("current")
_EnvironmentBranchATotalPower_Type = Integer32
_EnvironmentBranchATotalPower_Object = MibScalar
environmentBranchATotalPower = _EnvironmentBranchATotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 30),
    _EnvironmentBranchATotalPower_Type()
)
environmentBranchATotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchATotalPower.setStatus("current")
_EnvironmentBranchBTotalCurrent_Type = Integer32
_EnvironmentBranchBTotalCurrent_Object = MibScalar
environmentBranchBTotalCurrent = _EnvironmentBranchBTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 40),
    _EnvironmentBranchBTotalCurrent_Type()
)
environmentBranchBTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchBTotalCurrent.setStatus("current")
_EnvironmentBranchBTotalPower_Type = Integer32
_EnvironmentBranchBTotalPower_Object = MibScalar
environmentBranchBTotalPower = _EnvironmentBranchBTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 50),
    _EnvironmentBranchBTotalPower_Type()
)
environmentBranchBTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchBTotalPower.setStatus("current")
_EnvironmentBranchCTotalCurrent_Type = Integer32
_EnvironmentBranchCTotalCurrent_Object = MibScalar
environmentBranchCTotalCurrent = _EnvironmentBranchCTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 51),
    _EnvironmentBranchCTotalCurrent_Type()
)
environmentBranchCTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchCTotalCurrent.setStatus("current")
_EnvironmentBranchCTotalPower_Type = Integer32
_EnvironmentBranchCTotalPower_Object = MibScalar
environmentBranchCTotalPower = _EnvironmentBranchCTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 52),
    _EnvironmentBranchCTotalPower_Type()
)
environmentBranchCTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchCTotalPower.setStatus("current")
_EnvironmentBranchDTotalCurrent_Type = Integer32
_EnvironmentBranchDTotalCurrent_Object = MibScalar
environmentBranchDTotalCurrent = _EnvironmentBranchDTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 53),
    _EnvironmentBranchDTotalCurrent_Type()
)
environmentBranchDTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchDTotalCurrent.setStatus("current")
_EnvironmentBranchDTotalPower_Type = Integer32
_EnvironmentBranchDTotalPower_Object = MibScalar
environmentBranchDTotalPower = _EnvironmentBranchDTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 54),
    _EnvironmentBranchDTotalPower_Type()
)
environmentBranchDTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentBranchDTotalPower.setStatus("current")
_EnvironmentSystemTotalCurrent_Type = Integer32
_EnvironmentSystemTotalCurrent_Object = MibScalar
environmentSystemTotalCurrent = _EnvironmentSystemTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 60),
    _EnvironmentSystemTotalCurrent_Type()
)
environmentSystemTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentSystemTotalCurrent.setStatus("current")
_EnvironmentSystemTotalPower_Type = Integer32
_EnvironmentSystemTotalPower_Object = MibScalar
environmentSystemTotalPower = _EnvironmentSystemTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 70),
    _EnvironmentSystemTotalPower_Type()
)
environmentSystemTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentSystemTotalPower.setStatus("current")
_EnvironmentMonthlyPowerLog_Type = DisplayString
_EnvironmentMonthlyPowerLog_Object = MibScalar
environmentMonthlyPowerLog = _EnvironmentMonthlyPowerLog_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 200, 80),
    _EnvironmentMonthlyPowerLog_Type()
)
environmentMonthlyPowerLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    environmentMonthlyPowerLog.setStatus("current")
_WtiTraps_ObjectIdentity = ObjectIdentity
wtiTraps = _WtiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300)
)
_TrapInfo_Type = DisplayString
_TrapInfo_Object = MibScalar
trapInfo = _TrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 1),
    _TrapInfo_Type()
)
trapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapInfo.setStatus("current")
_TestTraps_ObjectIdentity = ObjectIdentity
testTraps = _TestTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 2)
)
_OverCurrentInitialTraps_ObjectIdentity = ObjectIdentity
overCurrentInitialTraps = _OverCurrentInitialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 4)
)
_OverCurrentCriticalTraps_ObjectIdentity = ObjectIdentity
overCurrentCriticalTraps = _OverCurrentCriticalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 5)
)
_OverTemperatureInitialTraps_ObjectIdentity = ObjectIdentity
overTemperatureInitialTraps = _OverTemperatureInitialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 6)
)
_OverTemperatureCriticalTraps_ObjectIdentity = ObjectIdentity
overTemperatureCriticalTraps = _OverTemperatureCriticalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 7)
)
_CircuitBreakerOpenTraps_ObjectIdentity = ObjectIdentity
circuitBreakerOpenTraps = _CircuitBreakerOpenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 8)
)
_LostCommTraps_ObjectIdentity = ObjectIdentity
lostCommTraps = _LostCommTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 9)
)
_LostVoltageTraps_ObjectIdentity = ObjectIdentity
lostVoltageTraps = _LostVoltageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 10)
)
_PingNoAnswerTraps_ObjectIdentity = ObjectIdentity
pingNoAnswerTraps = _PingNoAnswerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 11)
)
_LockoutTraps_ObjectIdentity = ObjectIdentity
lockoutTraps = _LockoutTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 12)
)
_PowercycleTraps_ObjectIdentity = ObjectIdentity
powercycleTraps = _PowercycleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 13)
)

# Managed Objects groups


# Notification objects

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 2, 0, 1)
)
testTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        ""
    )

overCurrentInitialSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 4, 0, 1)
)
overCurrentInitialSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overCurrentInitialSetTrap.setStatus(
        ""
    )

overCurrentInitialClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 4, 0, 2)
)
overCurrentInitialClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overCurrentInitialClearTrap.setStatus(
        ""
    )

overCurrentCriticalSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 5, 0, 1)
)
overCurrentCriticalSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overCurrentCriticalSetTrap.setStatus(
        ""
    )

overCurrentCriticalClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 5, 0, 2)
)
overCurrentCriticalClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overCurrentCriticalClearTrap.setStatus(
        ""
    )

overTemperatureInitialSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 6, 0, 1)
)
overTemperatureInitialSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureInitialSetTrap.setStatus(
        ""
    )

overTemperatureInitialClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 6, 0, 2)
)
overTemperatureInitialClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureInitialClearTrap.setStatus(
        ""
    )

overTemperatureCriticalSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 7, 0, 1)
)
overTemperatureCriticalSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureCriticalSetTrap.setStatus(
        ""
    )

overTemperatureCriticalClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 7, 0, 2)
)
overTemperatureCriticalClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    overTemperatureCriticalClearTrap.setStatus(
        ""
    )

circuitBreakerOpenSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 8, 0, 1)
)
circuitBreakerOpenSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    circuitBreakerOpenSetTrap.setStatus(
        ""
    )

circuitBreakerOpenClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 8, 0, 2)
)
circuitBreakerOpenClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    circuitBreakerOpenClearTrap.setStatus(
        ""
    )

lostCommSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 9, 0, 1)
)
lostCommSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lostCommSetTrap.setStatus(
        ""
    )

lostCommClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 9, 0, 2)
)
lostCommClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lostCommClearTrap.setStatus(
        ""
    )

lostVoltageSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 10, 0, 1)
)
lostVoltageSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lostVoltageSetTrap.setStatus(
        ""
    )

lostVoltageClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 10, 0, 2)
)
lostVoltageClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lostVoltageClearTrap.setStatus(
        ""
    )

pingNoAnswerSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 11, 0, 1)
)
pingNoAnswerSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    pingNoAnswerSetTrap.setStatus(
        ""
    )

pingNoAnswerClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 11, 0, 2)
)
pingNoAnswerClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    pingNoAnswerClearTrap.setStatus(
        ""
    )

lockoutSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 12, 0, 1)
)
lockoutSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lockoutSetTrap.setStatus(
        ""
    )

lockoutClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 12, 0, 2)
)
lockoutClearTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    lockoutClearTrap.setStatus(
        ""
    )

powercycleSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2634, 3, 300, 13, 0, 1)
)
powercycleSetTrap.setObjects(
    ("WTI-MPC-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    powercycleSetTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WTI-MPC-MIB",
    **{"westernTelematic": westernTelematic,
       "wti": wti,
       "systemTables": systemTables,
       "plugTable": plugTable,
       "plugEntry": plugEntry,
       "plugIndex": plugIndex,
       "plugID": plugID,
       "plugStatus": plugStatus,
       "plugAction": plugAction,
       "plugName": plugName,
       "plugGroupTable": plugGroupTable,
       "plugGroupEntry": plugGroupEntry,
       "plugGroupIndex": plugGroupIndex,
       "plugGroupName": plugGroupName,
       "plugGroupAction": plugGroupAction,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userName": userName,
       "userPasswd": userPasswd,
       "userAccessLevel": userAccessLevel,
       "userPortAccess": userPortAccess,
       "userLocalAccess": userLocalAccess,
       "userAux1Access": userAux1Access,
       "userAux2Access": userAux2Access,
       "userAux3Access": userAux3Access,
       "userGroupAccess": userGroupAccess,
       "userSerialAccess": userSerialAccess,
       "userTelnetSshAccess": userTelnetSshAccess,
       "userWebAccess": userWebAccess,
       "userCurrentPowerMetering": userCurrentPowerMetering,
       "userCallbackNum": userCallbackNum,
       "userSubmit": userSubmit,
       "environmentTables": environmentTables,
       "environmentUnitTable": environmentUnitTable,
       "environmentUnitEntry": environmentUnitEntry,
       "environmentUnitIndex": environmentUnitIndex,
       "environmentUnitName": environmentUnitName,
       "environmentUnitTemperature": environmentUnitTemperature,
       "environmentUnitCurrentA": environmentUnitCurrentA,
       "environmentUnitVoltageA": environmentUnitVoltageA,
       "environmentUnitPowerA": environmentUnitPowerA,
       "environmentUnitCurrentB": environmentUnitCurrentB,
       "environmentUnitVoltageB": environmentUnitVoltageB,
       "environmentUnitPowerB": environmentUnitPowerB,
       "environmentUnitCurrentC": environmentUnitCurrentC,
       "environmentUnitVoltageC": environmentUnitVoltageC,
       "environmentUnitPowerC": environmentUnitPowerC,
       "environmentUnitCurrentD": environmentUnitCurrentD,
       "environmentUnitVoltageD": environmentUnitVoltageD,
       "environmentUnitPowerD": environmentUnitPowerD,
       "environmentBranchATotalCurrent": environmentBranchATotalCurrent,
       "environmentBranchATotalPower": environmentBranchATotalPower,
       "environmentBranchBTotalCurrent": environmentBranchBTotalCurrent,
       "environmentBranchBTotalPower": environmentBranchBTotalPower,
       "environmentBranchCTotalCurrent": environmentBranchCTotalCurrent,
       "environmentBranchCTotalPower": environmentBranchCTotalPower,
       "environmentBranchDTotalCurrent": environmentBranchDTotalCurrent,
       "environmentBranchDTotalPower": environmentBranchDTotalPower,
       "environmentSystemTotalCurrent": environmentSystemTotalCurrent,
       "environmentSystemTotalPower": environmentSystemTotalPower,
       "environmentMonthlyPowerLog": environmentMonthlyPowerLog,
       "wtiTraps": wtiTraps,
       "trapInfo": trapInfo,
       "testTraps": testTraps,
       "testTrap": testTrap,
       "overCurrentInitialTraps": overCurrentInitialTraps,
       "overCurrentInitialSetTrap": overCurrentInitialSetTrap,
       "overCurrentInitialClearTrap": overCurrentInitialClearTrap,
       "overCurrentCriticalTraps": overCurrentCriticalTraps,
       "overCurrentCriticalSetTrap": overCurrentCriticalSetTrap,
       "overCurrentCriticalClearTrap": overCurrentCriticalClearTrap,
       "overTemperatureInitialTraps": overTemperatureInitialTraps,
       "overTemperatureInitialSetTrap": overTemperatureInitialSetTrap,
       "overTemperatureInitialClearTrap": overTemperatureInitialClearTrap,
       "overTemperatureCriticalTraps": overTemperatureCriticalTraps,
       "overTemperatureCriticalSetTrap": overTemperatureCriticalSetTrap,
       "overTemperatureCriticalClearTrap": overTemperatureCriticalClearTrap,
       "circuitBreakerOpenTraps": circuitBreakerOpenTraps,
       "circuitBreakerOpenSetTrap": circuitBreakerOpenSetTrap,
       "circuitBreakerOpenClearTrap": circuitBreakerOpenClearTrap,
       "lostCommTraps": lostCommTraps,
       "lostCommSetTrap": lostCommSetTrap,
       "lostCommClearTrap": lostCommClearTrap,
       "lostVoltageTraps": lostVoltageTraps,
       "lostVoltageSetTrap": lostVoltageSetTrap,
       "lostVoltageClearTrap": lostVoltageClearTrap,
       "pingNoAnswerTraps": pingNoAnswerTraps,
       "pingNoAnswerSetTrap": pingNoAnswerSetTrap,
       "pingNoAnswerClearTrap": pingNoAnswerClearTrap,
       "lockoutTraps": lockoutTraps,
       "lockoutSetTrap": lockoutSetTrap,
       "lockoutClearTrap": lockoutClearTrap,
       "powercycleTraps": powercycleTraps,
       "powercycleSetTrap": powercycleSetTrap}
)
