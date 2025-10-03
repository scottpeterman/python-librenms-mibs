# SNMP MIB module (DLINKSW-STORM-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-STORM-CTRL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:53 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwStormCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25)
)
if mibBuilder.loadTexts:
    dlinkSwStormCtrlMIB.setRevisions(
        ("2013-06-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DStormCtlTrafficType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )



class DStormCtlThrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2),
          ("percentage", 3))
    )



class DStormCtlThrTypeValue(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DStormCtrlMIBNotifications_ObjectIdentity = ObjectIdentity
dStormCtrlMIBNotifications = _DStormCtrlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 0)
)
_DStormCtrlMIBObjects_ObjectIdentity = ObjectIdentity
dStormCtrlMIBObjects = _DStormCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1)
)
_DStormCtrlGentrl_ObjectIdentity = ObjectIdentity
dStormCtrlGentrl = _DStormCtrlGentrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1)
)


class _DStormCtrlNotifyEnable_Type(Integer32):
    """Custom type dStormCtrlNotifyEnable based on Integer32"""
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
        *(("none", 1),
          ("stormOccurred", 2),
          ("stormCleared", 3),
          ("both", 4))
    )


_DStormCtrlNotifyEnable_Type.__name__ = "Integer32"
_DStormCtrlNotifyEnable_Object = MibScalar
dStormCtrlNotifyEnable = _DStormCtrlNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 1),
    _DStormCtrlNotifyEnable_Type()
)
dStormCtrlNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStormCtrlNotifyEnable.setStatus("current")


class _DStormCtrlPollingInterval_Type(Unsigned32):
    """Custom type dStormCtrlPollingInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_DStormCtrlPollingInterval_Type.__name__ = "Unsigned32"
_DStormCtrlPollingInterval_Object = MibScalar
dStormCtrlPollingInterval = _DStormCtrlPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 2),
    _DStormCtrlPollingInterval_Type()
)
dStormCtrlPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStormCtrlPollingInterval.setStatus("current")


class _DStormCtrlPollingRetries_Type(Integer32):
    """Custom type dStormCtrlPollingRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 360),
    )


_DStormCtrlPollingRetries_Type.__name__ = "Integer32"
_DStormCtrlPollingRetries_Object = MibScalar
dStormCtrlPollingRetries = _DStormCtrlPollingRetries_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 3),
    _DStormCtrlPollingRetries_Type()
)
dStormCtrlPollingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStormCtrlPollingRetries.setStatus("current")
_DStormCtrlThresholdTable_Object = MibTable
dStormCtrlThresholdTable = _DStormCtrlThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2)
)
if mibBuilder.loadTexts:
    dStormCtrlThresholdTable.setStatus("current")
_DStormCtrlThresholdEntry_Object = MibTableRow
dStormCtrlThresholdEntry = _DStormCtrlThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1)
)
dStormCtrlThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"),
)
if mibBuilder.loadTexts:
    dStormCtrlThresholdEntry.setStatus("current")
_DStormCtrlTrafficType_Type = DStormCtlTrafficType
_DStormCtrlTrafficType_Object = MibTableColumn
dStormCtrlTrafficType = _DStormCtrlTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 1),
    _DStormCtrlTrafficType_Type()
)
dStormCtrlTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dStormCtrlTrafficType.setStatus("current")
_DStormCtrlThresholdType_Type = DStormCtlThrType
_DStormCtrlThresholdType_Object = MibTableColumn
dStormCtrlThresholdType = _DStormCtrlThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 2),
    _DStormCtrlThresholdType_Type()
)
dStormCtrlThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dStormCtrlThresholdType.setStatus("current")
_DStormCtrlRiseThresholdValue_Type = DStormCtlThrTypeValue
_DStormCtrlRiseThresholdValue_Object = MibTableColumn
dStormCtrlRiseThresholdValue = _DStormCtrlRiseThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 3),
    _DStormCtrlRiseThresholdValue_Type()
)
dStormCtrlRiseThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dStormCtrlRiseThresholdValue.setStatus("current")
_DStormCtrlLowThresholdValue_Type = DStormCtlThrTypeValue
_DStormCtrlLowThresholdValue_Object = MibTableColumn
dStormCtrlLowThresholdValue = _DStormCtrlLowThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 4),
    _DStormCtrlLowThresholdValue_Type()
)
dStormCtrlLowThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dStormCtrlLowThresholdValue.setStatus("current")
_DStormCtrlIfTable_Object = MibTable
dStormCtrlIfTable = _DStormCtrlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3)
)
if mibBuilder.loadTexts:
    dStormCtrlIfTable.setStatus("current")
_DStormCtrlIfEntry_Object = MibTableRow
dStormCtrlIfEntry = _DStormCtrlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1)
)
dStormCtrlIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dStormCtrlIfEntry.setStatus("current")


class _DStormCtrlIfActionType_Type(Integer32):
    """Custom type dStormCtrlIfActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("shutdown", 2),
          ("drop", 3))
    )


_DStormCtrlIfActionType_Type.__name__ = "Integer32"
_DStormCtrlIfActionType_Object = MibTableColumn
dStormCtrlIfActionType = _DStormCtrlIfActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1, 1),
    _DStormCtrlIfActionType_Type()
)
dStormCtrlIfActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStormCtrlIfActionType.setStatus("current")
_DStormCtrlTrafficInfoTable_Object = MibTable
dStormCtrlTrafficInfoTable = _DStormCtrlTrafficInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4)
)
if mibBuilder.loadTexts:
    dStormCtrlTrafficInfoTable.setStatus("current")
_DStormCtrlTrafficInfoEntry_Object = MibTableRow
dStormCtrlTrafficInfoEntry = _DStormCtrlTrafficInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1)
)
dStormCtrlTrafficInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"),
)
if mibBuilder.loadTexts:
    dStormCtrlTrafficInfoEntry.setStatus("current")
_DStormCtrlCurTrafficUnitType_Type = DStormCtlThrType
_DStormCtrlCurTrafficUnitType_Object = MibTableColumn
dStormCtrlCurTrafficUnitType = _DStormCtrlCurTrafficUnitType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 1),
    _DStormCtrlCurTrafficUnitType_Type()
)
dStormCtrlCurTrafficUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStormCtrlCurTrafficUnitType.setStatus("current")
_DStormCtrlCurTrafficValue_Type = DStormCtlThrTypeValue
_DStormCtrlCurTrafficValue_Object = MibTableColumn
dStormCtrlCurTrafficValue = _DStormCtrlCurTrafficValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 2),
    _DStormCtrlCurTrafficValue_Type()
)
dStormCtrlCurTrafficValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStormCtrlCurTrafficValue.setStatus("current")


class _DStormCtrlTrafficInfoStatus_Type(Integer32):
    """Custom type dStormCtrlTrafficInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("dropped", 2),
          ("errorDisabled", 3),
          ("linkDown", 4),
          ("inactive", 5))
    )


_DStormCtrlTrafficInfoStatus_Type.__name__ = "Integer32"
_DStormCtrlTrafficInfoStatus_Object = MibTableColumn
dStormCtrlTrafficInfoStatus = _DStormCtrlTrafficInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 3),
    _DStormCtrlTrafficInfoStatus_Type()
)
dStormCtrlTrafficInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStormCtrlTrafficInfoStatus.setStatus("current")
_DStormCtrlNotifyInfo_ObjectIdentity = ObjectIdentity
dStormCtrlNotifyInfo = _DStormCtrlNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5)
)
_DStormCtrlNotifyTrafficType_Type = DStormCtlTrafficType
_DStormCtrlNotifyTrafficType_Object = MibScalar
dStormCtrlNotifyTrafficType = _DStormCtrlNotifyTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5, 1),
    _DStormCtrlNotifyTrafficType_Type()
)
dStormCtrlNotifyTrafficType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dStormCtrlNotifyTrafficType.setStatus("current")
_DStormCtrlMIBConformance_ObjectIdentity = ObjectIdentity
dStormCtrlMIBConformance = _DStormCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2)
)
_DStormCtrlCompliances_ObjectIdentity = ObjectIdentity
dStormCtrlCompliances = _DStormCtrlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1)
)
_DStormCtrlGroup_ObjectIdentity = ObjectIdentity
dStormCtrlGroup = _DStormCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2)
)

# Managed Objects groups

dStormCtrlBaiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 1)
)
dStormCtrlBaiscGroup.setObjects(
      *(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyEnable"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingInterval"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingRetries"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlThresholdType"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlRiseThresholdValue"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlLowThresholdValue"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlIfActionType"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficUnitType"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficValue"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficInfoStatus"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
)
if mibBuilder.loadTexts:
    dStormCtrlBaiscGroup.setStatus("current")


# Notification objects

dStormCtrlOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 1)
)
dStormCtrlOccurred.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
)
if mibBuilder.loadTexts:
    dStormCtrlOccurred.setStatus(
        "current"
    )

dStormCtrlStormCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 2)
)
dStormCtrlStormCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
)
if mibBuilder.loadTexts:
    dStormCtrlStormCleared.setStatus(
        "current"
    )


# Notifications groups

dStormCtrlNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 2)
)
dStormCtrlNotifyGroup.setObjects(
      *(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlOccurred"),
        ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlStormCleared"))
)
if mibBuilder.loadTexts:
    dStormCtrlNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dStormCtrlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1, 1)
)
dStormCtrlCompliance.setObjects(
    ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlBaiscGroup")
)
if mibBuilder.loadTexts:
    dStormCtrlCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-STORM-CTRL-MIB",
    **{"DStormCtlTrafficType": DStormCtlTrafficType,
       "DStormCtlThrType": DStormCtlThrType,
       "DStormCtlThrTypeValue": DStormCtlThrTypeValue,
       "dlinkSwStormCtrlMIB": dlinkSwStormCtrlMIB,
       "dStormCtrlMIBNotifications": dStormCtrlMIBNotifications,
       "dStormCtrlOccurred": dStormCtrlOccurred,
       "dStormCtrlStormCleared": dStormCtrlStormCleared,
       "dStormCtrlMIBObjects": dStormCtrlMIBObjects,
       "dStormCtrlGentrl": dStormCtrlGentrl,
       "dStormCtrlNotifyEnable": dStormCtrlNotifyEnable,
       "dStormCtrlPollingInterval": dStormCtrlPollingInterval,
       "dStormCtrlPollingRetries": dStormCtrlPollingRetries,
       "dStormCtrlThresholdTable": dStormCtrlThresholdTable,
       "dStormCtrlThresholdEntry": dStormCtrlThresholdEntry,
       "dStormCtrlTrafficType": dStormCtrlTrafficType,
       "dStormCtrlThresholdType": dStormCtrlThresholdType,
       "dStormCtrlRiseThresholdValue": dStormCtrlRiseThresholdValue,
       "dStormCtrlLowThresholdValue": dStormCtrlLowThresholdValue,
       "dStormCtrlIfTable": dStormCtrlIfTable,
       "dStormCtrlIfEntry": dStormCtrlIfEntry,
       "dStormCtrlIfActionType": dStormCtrlIfActionType,
       "dStormCtrlTrafficInfoTable": dStormCtrlTrafficInfoTable,
       "dStormCtrlTrafficInfoEntry": dStormCtrlTrafficInfoEntry,
       "dStormCtrlCurTrafficUnitType": dStormCtrlCurTrafficUnitType,
       "dStormCtrlCurTrafficValue": dStormCtrlCurTrafficValue,
       "dStormCtrlTrafficInfoStatus": dStormCtrlTrafficInfoStatus,
       "dStormCtrlNotifyInfo": dStormCtrlNotifyInfo,
       "dStormCtrlNotifyTrafficType": dStormCtrlNotifyTrafficType,
       "dStormCtrlMIBConformance": dStormCtrlMIBConformance,
       "dStormCtrlCompliances": dStormCtrlCompliances,
       "dStormCtrlCompliance": dStormCtrlCompliance,
       "dStormCtrlGroup": dStormCtrlGroup,
       "dStormCtrlBaiscGroup": dStormCtrlBaiscGroup,
       "dStormCtrlNotifyGroup": dStormCtrlNotifyGroup}
)
