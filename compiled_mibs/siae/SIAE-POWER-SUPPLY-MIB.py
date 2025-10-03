# SNMP MIB module (SIAE-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-POWER-SUPPLY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:22 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pwrSupply = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89)
)
if mibBuilder.loadTexts:
    pwrSupply.setRevisions(
        ("2014-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PwrSupplyMibVersion_Type(Integer32):
    """Custom type pwrSupplyMibVersion based on Integer32"""
    defaultValue = 1


_PwrSupplyMibVersion_Type.__name__ = "Integer32"
_PwrSupplyMibVersion_Object = MibScalar
pwrSupplyMibVersion = _PwrSupplyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 1),
    _PwrSupplyMibVersion_Type()
)
pwrSupplyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyMibVersion.setStatus("current")
_PwrSupplyTable_Object = MibTable
pwrSupplyTable = _PwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2)
)
if mibBuilder.loadTexts:
    pwrSupplyTable.setStatus("current")
_PwrSupplyTableEntry_Object = MibTableRow
pwrSupplyTableEntry = _PwrSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1)
)
pwrSupplyTableEntry.setIndexNames(
    (0, "SIAE-POWER-SUPPLY-MIB", "pwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    pwrSupplyTableEntry.setStatus("current")
_PwrSupplyIndex_Type = Integer32
_PwrSupplyIndex_Object = MibTableColumn
pwrSupplyIndex = _PwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1, 1),
    _PwrSupplyIndex_Type()
)
pwrSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwrSupplyIndex.setStatus("current")
_PwrSupplyRowStatus_Type = RowStatus
_PwrSupplyRowStatus_Object = MibTableColumn
pwrSupplyRowStatus = _PwrSupplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1, 2),
    _PwrSupplyRowStatus_Type()
)
pwrSupplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwrSupplyRowStatus.setStatus("current")


class _PwrSupplyLabel_Type(DisplayString):
    """Custom type pwrSupplyLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PwrSupplyLabel_Type.__name__ = "DisplayString"
_PwrSupplyLabel_Object = MibTableColumn
pwrSupplyLabel = _PwrSupplyLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1, 3),
    _PwrSupplyLabel_Type()
)
pwrSupplyLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyLabel.setStatus("current")


class _PwrSupplyAdminStatus_Type(Integer32):
    """Custom type pwrSupplyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PwrSupplyAdminStatus_Type.__name__ = "Integer32"
_PwrSupplyAdminStatus_Object = MibTableColumn
pwrSupplyAdminStatus = _PwrSupplyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1, 4),
    _PwrSupplyAdminStatus_Type()
)
pwrSupplyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwrSupplyAdminStatus.setStatus("current")
_PwrSupplyAlarm_Type = AlarmStatus
_PwrSupplyAlarm_Object = MibTableColumn
pwrSupplyAlarm = _PwrSupplyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 2, 1, 5),
    _PwrSupplyAlarm_Type()
)
pwrSupplyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyAlarm.setStatus("current")


class _PwrSupplyAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type pwrSupplyAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PwrSupplyAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PwrSupplyAlarmSeverityCode_Object = MibScalar
pwrSupplyAlarmSeverityCode = _PwrSupplyAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 89, 3),
    _PwrSupplyAlarmSeverityCode_Type()
)
pwrSupplyAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrSupplyAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-POWER-SUPPLY-MIB",
    **{"pwrSupply": pwrSupply,
       "pwrSupplyMibVersion": pwrSupplyMibVersion,
       "pwrSupplyTable": pwrSupplyTable,
       "pwrSupplyTableEntry": pwrSupplyTableEntry,
       "pwrSupplyIndex": pwrSupplyIndex,
       "pwrSupplyRowStatus": pwrSupplyRowStatus,
       "pwrSupplyLabel": pwrSupplyLabel,
       "pwrSupplyAdminStatus": pwrSupplyAdminStatus,
       "pwrSupplyAlarm": pwrSupplyAlarm,
       "pwrSupplyAlarmSeverityCode": pwrSupplyAlarmSeverityCode}
)
