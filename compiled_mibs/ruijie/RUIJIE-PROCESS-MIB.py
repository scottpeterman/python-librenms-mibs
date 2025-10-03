# SNMP MIB module (RUIJIE-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruijie\RUIJIE-PROCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:27 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36)
)
if mibBuilder.loadTexts:
    ruijieProcessMIB.setRevisions(
        ("2003-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_RuijieCPUMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCPUMIBObjects = _RuijieCPUMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1)
)
_RuijieCpuGeneralMibsGroup_ObjectIdentity = ObjectIdentity
ruijieCpuGeneralMibsGroup = _RuijieCpuGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1)
)
_RuijieCPUUtilization5Sec_Type = Percent
_RuijieCPUUtilization5Sec_Object = MibScalar
ruijieCPUUtilization5Sec = _RuijieCPUUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 1),
    _RuijieCPUUtilization5Sec_Type()
)
ruijieCPUUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUUtilization5Sec.setStatus("current")
_RuijieCPUUtilization1Min_Type = Percent
_RuijieCPUUtilization1Min_Object = MibScalar
ruijieCPUUtilization1Min = _RuijieCPUUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 2),
    _RuijieCPUUtilization1Min_Type()
)
ruijieCPUUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUUtilization1Min.setStatus("current")
_RuijieCPUUtilization5Min_Type = Percent
_RuijieCPUUtilization5Min_Object = MibScalar
ruijieCPUUtilization5Min = _RuijieCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 3),
    _RuijieCPUUtilization5Min_Type()
)
ruijieCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUUtilization5Min.setStatus("current")
_RuijieCPUUtilizationWarning_Type = Percent
_RuijieCPUUtilizationWarning_Object = MibScalar
ruijieCPUUtilizationWarning = _RuijieCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 4),
    _RuijieCPUUtilizationWarning_Type()
)
ruijieCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCPUUtilizationWarning.setStatus("current")
_RuijieCPUUtilizationCritical_Type = Percent
_RuijieCPUUtilizationCritical_Object = MibScalar
ruijieCPUUtilizationCritical = _RuijieCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 5),
    _RuijieCPUUtilizationCritical_Type()
)
ruijieCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCPUUtilizationCritical.setStatus("current")
_RuijieCPUMaxUtilization5Sec_Type = Percent
_RuijieCPUMaxUtilization5Sec_Object = MibScalar
ruijieCPUMaxUtilization5Sec = _RuijieCPUMaxUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 6),
    _RuijieCPUMaxUtilization5Sec_Type()
)
ruijieCPUMaxUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUMaxUtilization5Sec.setStatus("current")
_RuijieCPUMaxUtilization1Min_Type = Percent
_RuijieCPUMaxUtilization1Min_Object = MibScalar
ruijieCPUMaxUtilization1Min = _RuijieCPUMaxUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 7),
    _RuijieCPUMaxUtilization1Min_Type()
)
ruijieCPUMaxUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUMaxUtilization1Min.setStatus("current")
_RuijieCPUMaxUtilization5Min_Type = Percent
_RuijieCPUMaxUtilization5Min_Object = MibScalar
ruijieCPUMaxUtilization5Min = _RuijieCPUMaxUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 8),
    _RuijieCPUMaxUtilization5Min_Type()
)
ruijieCPUMaxUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUMaxUtilization5Min.setStatus("current")
_RuijieCPUUtilizationCollectSwitch_Type = Integer32
_RuijieCPUUtilizationCollectSwitch_Object = MibScalar
ruijieCPUUtilizationCollectSwitch = _RuijieCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 9),
    _RuijieCPUUtilizationCollectSwitch_Type()
)
ruijieCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCPUUtilizationCollectSwitch.setStatus("current")
_RuijieCPUUtilizationCurrent_Type = Percent
_RuijieCPUUtilizationCurrent_Object = MibScalar
ruijieCPUUtilizationCurrent = _RuijieCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 1, 10),
    _RuijieCPUUtilizationCurrent_Type()
)
ruijieCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCPUUtilizationCurrent.setStatus("current")
_RuijieNodeCPUTotalTable_Object = MibTable
ruijieNodeCPUTotalTable = _RuijieNodeCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalTable.setStatus("current")
_RuijieNodeCPUTotalEntry_Object = MibTableRow
ruijieNodeCPUTotalEntry = _RuijieNodeCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1)
)
ruijieNodeCPUTotalEntry.setIndexNames(
    (0, "RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalEntry.setStatus("current")


class _RuijieNodeCPUTotalIndex_Type(Integer32):
    """Custom type ruijieNodeCPUTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieNodeCPUTotalIndex_Type.__name__ = "Integer32"
_RuijieNodeCPUTotalIndex_Object = MibTableColumn
ruijieNodeCPUTotalIndex = _RuijieNodeCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 1),
    _RuijieNodeCPUTotalIndex_Type()
)
ruijieNodeCPUTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalIndex.setStatus("current")
_RuijieNodeCPUTotalName_Type = DisplayString
_RuijieNodeCPUTotalName_Object = MibTableColumn
ruijieNodeCPUTotalName = _RuijieNodeCPUTotalName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 2),
    _RuijieNodeCPUTotalName_Type()
)
ruijieNodeCPUTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalName.setStatus("current")
_RuijieNodeCPUTotal5sec_Type = Percent
_RuijieNodeCPUTotal5sec_Object = MibTableColumn
ruijieNodeCPUTotal5sec = _RuijieNodeCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 3),
    _RuijieNodeCPUTotal5sec_Type()
)
ruijieNodeCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotal5sec.setStatus("current")
_RuijieNodeCPUTotal1min_Type = Percent
_RuijieNodeCPUTotal1min_Object = MibTableColumn
ruijieNodeCPUTotal1min = _RuijieNodeCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 4),
    _RuijieNodeCPUTotal1min_Type()
)
ruijieNodeCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotal1min.setStatus("current")
_RuijieNodeCPUTotal5min_Type = Percent
_RuijieNodeCPUTotal5min_Object = MibTableColumn
ruijieNodeCPUTotal5min = _RuijieNodeCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 5),
    _RuijieNodeCPUTotal5min_Type()
)
ruijieNodeCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotal5min.setStatus("current")
_RuijieNodeCPUTotalWarning_Type = Percent
_RuijieNodeCPUTotalWarning_Object = MibTableColumn
ruijieNodeCPUTotalWarning = _RuijieNodeCPUTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 6),
    _RuijieNodeCPUTotalWarning_Type()
)
ruijieNodeCPUTotalWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalWarning.setStatus("current")
_RuijieNodeCPUTotalCritical_Type = Percent
_RuijieNodeCPUTotalCritical_Object = MibTableColumn
ruijieNodeCPUTotalCritical = _RuijieNodeCPUTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 2, 1, 7),
    _RuijieNodeCPUTotalCritical_Type()
)
ruijieNodeCPUTotalCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalCritical.setStatus("current")
_RuijieLankApCPUTotalTable_Object = MibTable
ruijieLankApCPUTotalTable = _RuijieLankApCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieLankApCPUTotalTable.setStatus("current")
_RuijieLankApCPUTotalEntry_Object = MibTableRow
ruijieLankApCPUTotalEntry = _RuijieLankApCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1)
)
ruijieLankApCPUTotalEntry.setIndexNames(
    (0, "RUIJIE-PROCESS-MIB", "ruijieLankApCPUMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieLankApCPUTotalEntry.setStatus("current")
_RuijieLankApCPUMacAddr_Type = MacAddress
_RuijieLankApCPUMacAddr_Object = MibTableColumn
ruijieLankApCPUMacAddr = _RuijieLankApCPUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 1),
    _RuijieLankApCPUMacAddr_Type()
)
ruijieLankApCPUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApCPUMacAddr.setStatus("current")
_RuijieLankApCPUUtilizationCollectSwitch_Type = Integer32
_RuijieLankApCPUUtilizationCollectSwitch_Object = MibTableColumn
ruijieLankApCPUUtilizationCollectSwitch = _RuijieLankApCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 2),
    _RuijieLankApCPUUtilizationCollectSwitch_Type()
)
ruijieLankApCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLankApCPUUtilizationCollectSwitch.setStatus("current")
_RuijieLankApCPUUtilizationWarning_Type = Percent
_RuijieLankApCPUUtilizationWarning_Object = MibTableColumn
ruijieLankApCPUUtilizationWarning = _RuijieLankApCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 3),
    _RuijieLankApCPUUtilizationWarning_Type()
)
ruijieLankApCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLankApCPUUtilizationWarning.setStatus("current")
_RuijieLankApCPUUtilizationCritical_Type = Percent
_RuijieLankApCPUUtilizationCritical_Object = MibTableColumn
ruijieLankApCPUUtilizationCritical = _RuijieLankApCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 4),
    _RuijieLankApCPUUtilizationCritical_Type()
)
ruijieLankApCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLankApCPUUtilizationCritical.setStatus("current")
_RuijieLankApCPUUtilizationCurrent_Type = Percent
_RuijieLankApCPUUtilizationCurrent_Object = MibTableColumn
ruijieLankApCPUUtilizationCurrent = _RuijieLankApCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 5),
    _RuijieLankApCPUUtilizationCurrent_Type()
)
ruijieLankApCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApCPUUtilizationCurrent.setStatus("current")
_RuijieLankApCPUUtilization5Min_Type = Percent
_RuijieLankApCPUUtilization5Min_Object = MibTableColumn
ruijieLankApCPUUtilization5Min = _RuijieLankApCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 1, 3, 1, 6),
    _RuijieLankApCPUUtilization5Min_Type()
)
ruijieLankApCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLankApCPUUtilization5Min.setStatus("current")
_RuijieProcessMIBConformance_ObjectIdentity = ObjectIdentity
ruijieProcessMIBConformance = _RuijieProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2)
)
_RuijieProcessMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieProcessMIBCompliances = _RuijieProcessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2, 1)
)
_RuijieProcessMIBGroups_ObjectIdentity = ObjectIdentity
ruijieProcessMIBGroups = _RuijieProcessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2, 2)
)

# Managed Objects groups

ruijieCPUUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2, 2, 1)
)
ruijieCPUUtilizationMIBGroup.setObjects(
      *(("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization5Sec"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization1Min"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilization5Min"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUMaxUtilization5Sec"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUMaxUtilization1Min"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUMaxUtilization5Min"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilizationCollectSwitch"),
        ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilizationCurrent"))
)
if mibBuilder.loadTexts:
    ruijieCPUUtilizationMIBGroup.setStatus("current")

ruijieNodeCPUTotalGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2, 2, 2)
)
ruijieNodeCPUTotalGroups.setObjects(
      *(("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalIndex"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalName"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotal5sec"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotal1min"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotal5min"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalWarning"),
        ("RUIJIE-PROCESS-MIB", "ruijieNodeCPUTotalCritical"))
)
if mibBuilder.loadTexts:
    ruijieNodeCPUTotalGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 36, 2, 1, 1)
)
ruijieProcessMIBCompliance.setObjects(
    ("RUIJIE-PROCESS-MIB", "ruijieCPUUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PROCESS-MIB",
    **{"Percent": Percent,
       "ruijieProcessMIB": ruijieProcessMIB,
       "ruijieCPUMIBObjects": ruijieCPUMIBObjects,
       "ruijieCpuGeneralMibsGroup": ruijieCpuGeneralMibsGroup,
       "ruijieCPUUtilization5Sec": ruijieCPUUtilization5Sec,
       "ruijieCPUUtilization1Min": ruijieCPUUtilization1Min,
       "ruijieCPUUtilization5Min": ruijieCPUUtilization5Min,
       "ruijieCPUUtilizationWarning": ruijieCPUUtilizationWarning,
       "ruijieCPUUtilizationCritical": ruijieCPUUtilizationCritical,
       "ruijieCPUMaxUtilization5Sec": ruijieCPUMaxUtilization5Sec,
       "ruijieCPUMaxUtilization1Min": ruijieCPUMaxUtilization1Min,
       "ruijieCPUMaxUtilization5Min": ruijieCPUMaxUtilization5Min,
       "ruijieCPUUtilizationCollectSwitch": ruijieCPUUtilizationCollectSwitch,
       "ruijieCPUUtilizationCurrent": ruijieCPUUtilizationCurrent,
       "ruijieNodeCPUTotalTable": ruijieNodeCPUTotalTable,
       "ruijieNodeCPUTotalEntry": ruijieNodeCPUTotalEntry,
       "ruijieNodeCPUTotalIndex": ruijieNodeCPUTotalIndex,
       "ruijieNodeCPUTotalName": ruijieNodeCPUTotalName,
       "ruijieNodeCPUTotal5sec": ruijieNodeCPUTotal5sec,
       "ruijieNodeCPUTotal1min": ruijieNodeCPUTotal1min,
       "ruijieNodeCPUTotal5min": ruijieNodeCPUTotal5min,
       "ruijieNodeCPUTotalWarning": ruijieNodeCPUTotalWarning,
       "ruijieNodeCPUTotalCritical": ruijieNodeCPUTotalCritical,
       "ruijieLankApCPUTotalTable": ruijieLankApCPUTotalTable,
       "ruijieLankApCPUTotalEntry": ruijieLankApCPUTotalEntry,
       "ruijieLankApCPUMacAddr": ruijieLankApCPUMacAddr,
       "ruijieLankApCPUUtilizationCollectSwitch": ruijieLankApCPUUtilizationCollectSwitch,
       "ruijieLankApCPUUtilizationWarning": ruijieLankApCPUUtilizationWarning,
       "ruijieLankApCPUUtilizationCritical": ruijieLankApCPUUtilizationCritical,
       "ruijieLankApCPUUtilizationCurrent": ruijieLankApCPUUtilizationCurrent,
       "ruijieLankApCPUUtilization5Min": ruijieLankApCPUUtilization5Min,
       "ruijieProcessMIBConformance": ruijieProcessMIBConformance,
       "ruijieProcessMIBCompliances": ruijieProcessMIBCompliances,
       "ruijieProcessMIBCompliance": ruijieProcessMIBCompliance,
       "ruijieProcessMIBGroups": ruijieProcessMIBGroups,
       "ruijieCPUUtilizationMIBGroup": ruijieCPUUtilizationMIBGroup,
       "ruijieNodeCPUTotalGroups": ruijieNodeCPUTotalGroups}
)
