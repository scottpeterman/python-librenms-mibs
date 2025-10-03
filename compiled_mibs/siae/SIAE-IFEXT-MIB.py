# SNMP MIB module (SIAE-IFEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-IFEXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:03 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ifext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73)
)
if mibBuilder.loadTexts:
    ifext.setRevisions(
        ("2016-04-18 00:00",
         "2015-07-21 00:00",
         "2014-12-02 00:00",
         "2014-09-26 00:00",
         "2014-06-05 00:00",
         "2014-02-21 00:00",
         "2013-10-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _IfextMibVersion_Type(Integer32):
    """Custom type ifextMibVersion based on Integer32"""
    defaultValue = 1


_IfextMibVersion_Type.__name__ = "Integer32"
_IfextMibVersion_Object = MibScalar
ifextMibVersion = _IfextMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 1),
    _IfextMibVersion_Type()
)
ifextMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextMibVersion.setStatus("current")
_IfextTable_Object = MibTable
ifextTable = _IfextTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2)
)
if mibBuilder.loadTexts:
    ifextTable.setStatus("current")
_IfextTableEntry_Object = MibTableRow
ifextTableEntry = _IfextTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1)
)
ifextTableEntry.setIndexNames(
    (0, "SIAE-IFEXT-MIB", "ifextIfIndex"),
)
if mibBuilder.loadTexts:
    ifextTableEntry.setStatus("current")
_IfextIfIndex_Type = InterfaceIndex
_IfextIfIndex_Object = MibTableColumn
ifextIfIndex = _IfextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 1),
    _IfextIfIndex_Type()
)
ifextIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifextIfIndex.setStatus("current")


class _IfextLabel_Type(DisplayString):
    """Custom type ifextLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IfextLabel_Type.__name__ = "DisplayString"
_IfextLabel_Object = MibTableColumn
ifextLabel = _IfextLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 2),
    _IfextLabel_Type()
)
ifextLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextLabel.setStatus("current")


class _IfextAdminStatus_Type(Integer32):
    """Custom type ifextAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("loopback", 4))
    )


_IfextAdminStatus_Type.__name__ = "Integer32"
_IfextAdminStatus_Object = MibTableColumn
ifextAdminStatus = _IfextAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 3),
    _IfextAdminStatus_Type()
)
ifextAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextAdminStatus.setStatus("current")


class _IfextPortUsage_Type(Integer32):
    """Custom type ifextPortUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("lan", 1),
          ("radio", 2),
          ("mgmt", 3),
          ("stack", 4),
          ("aux", 5),
          ("pwe3", 6))
    )


_IfextPortUsage_Type.__name__ = "Integer32"
_IfextPortUsage_Object = MibTableColumn
ifextPortUsage = _IfextPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 4),
    _IfextPortUsage_Type()
)
ifextPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextPortUsage.setStatus("current")


class _IfextMediumType_Type(Integer32):
    """Custom type ifextMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("combo", 3),
          ("other", 4))
    )


_IfextMediumType_Type.__name__ = "Integer32"
_IfextMediumType_Object = MibTableColumn
ifextMediumType = _IfextMediumType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 5),
    _IfextMediumType_Type()
)
ifextMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextMediumType.setStatus("current")


class _IfextMediumSelection_Type(Integer32):
    """Custom type ifextMediumSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("copper", 1),
          ("fiber", 2))
    )


_IfextMediumSelection_Type.__name__ = "Integer32"
_IfextMediumSelection_Object = MibTableColumn
ifextMediumSelection = _IfextMediumSelection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 6),
    _IfextMediumSelection_Type()
)
ifextMediumSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextMediumSelection.setStatus("current")


class _IfextAlarmReportEnable_Type(Integer32):
    """Custom type ifextAlarmReportEnable based on Integer32"""
    defaultValue = 2

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


_IfextAlarmReportEnable_Type.__name__ = "Integer32"
_IfextAlarmReportEnable_Object = MibTableColumn
ifextAlarmReportEnable = _IfextAlarmReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 7),
    _IfextAlarmReportEnable_Type()
)
ifextAlarmReportEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifextAlarmReportEnable.setStatus("current")
_IfextSfpId_Type = Integer32
_IfextSfpId_Object = MibTableColumn
ifextSfpId = _IfextSfpId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 8),
    _IfextSfpId_Type()
)
ifextSfpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextSfpId.setStatus("current")


class _IfextCapabilities_Type(Bits):
    """Custom type ifextCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ifextCapabilityLoop", 0),
          ("ifextCapability2g5Bps", 1),
          ("ifextCapabilityMabSensor", 2),
          ("ifextCapabilityEncrypt", 3),
          ("ifextCapability10gBps", 4))
    )

_IfextCapabilities_Type.__name__ = "Bits"
_IfextCapabilities_Object = MibTableColumn
ifextCapabilities = _IfextCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 9),
    _IfextCapabilities_Type()
)
ifextCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextCapabilities.setStatus("current")
_IfextLosAlarm_Type = AlarmStatus
_IfextLosAlarm_Object = MibTableColumn
ifextLosAlarm = _IfextLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 10),
    _IfextLosAlarm_Type()
)
ifextLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextLosAlarm.setStatus("current")
_IfextRowStatus_Type = RowStatus
_IfextRowStatus_Object = MibTableColumn
ifextRowStatus = _IfextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 11),
    _IfextRowStatus_Type()
)
ifextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifextRowStatus.setStatus("current")
_IfextMaintTable_Object = MibTable
ifextMaintTable = _IfextMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3)
)
if mibBuilder.loadTexts:
    ifextMaintTable.setStatus("current")
_IfextMaintTableEntry_Object = MibTableRow
ifextMaintTableEntry = _IfextMaintTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1)
)
ifextMaintTableEntry.setIndexNames(
    (0, "SIAE-IFEXT-MIB", "ifextIfIndex"),
)
if mibBuilder.loadTexts:
    ifextMaintTableEntry.setStatus("current")


class _IfextLineLoop_Type(Integer32):
    """Custom type ifextLineLoop based on Integer32"""
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


_IfextLineLoop_Type.__name__ = "Integer32"
_IfextLineLoop_Object = MibTableColumn
ifextLineLoop = _IfextLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1, 1),
    _IfextLineLoop_Type()
)
ifextLineLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifextLineLoop.setStatus("current")


class _IfextLosAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ifextLosAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_IfextLosAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_IfextLosAlarmSeverityCode_Object = MibScalar
ifextLosAlarmSeverityCode = _IfextLosAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 73, 5),
    _IfextLosAlarmSeverityCode_Type()
)
ifextLosAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifextLosAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-IFEXT-MIB",
    **{"ifext": ifext,
       "ifextMibVersion": ifextMibVersion,
       "ifextTable": ifextTable,
       "ifextTableEntry": ifextTableEntry,
       "ifextIfIndex": ifextIfIndex,
       "ifextLabel": ifextLabel,
       "ifextAdminStatus": ifextAdminStatus,
       "ifextPortUsage": ifextPortUsage,
       "ifextMediumType": ifextMediumType,
       "ifextMediumSelection": ifextMediumSelection,
       "ifextAlarmReportEnable": ifextAlarmReportEnable,
       "ifextSfpId": ifextSfpId,
       "ifextCapabilities": ifextCapabilities,
       "ifextLosAlarm": ifextLosAlarm,
       "ifextRowStatus": ifextRowStatus,
       "ifextMaintTable": ifextMaintTable,
       "ifextMaintTableEntry": ifextMaintTableEntry,
       "ifextLineLoop": ifextLineLoop,
       "ifextLosAlarmSeverityCode": ifextLosAlarmSeverityCode}
)
