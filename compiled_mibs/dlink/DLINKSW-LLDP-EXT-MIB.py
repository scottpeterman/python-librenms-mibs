# SNMP MIB module (DLINKSW-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-LLDP-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:31 2025
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

(lldpLocPortNum,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocPortNum")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwLldpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20)
)
if mibBuilder.loadTexts:
    dlinkSwLldpExtMIB.setRevisions(
        ("2013-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DLldpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dLldpExtMIBNotifications = _DLldpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 0)
)
_DLldpExtMIBObjects_ObjectIdentity = ObjectIdentity
dLldpExtMIBObjects = _DLldpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1)
)
_DLldpExtLldpEnabled_Type = TruthValue
_DLldpExtLldpEnabled_Object = MibScalar
dLldpExtLldpEnabled = _DLldpExtLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 1),
    _DLldpExtLldpEnabled_Type()
)
dLldpExtLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtLldpEnabled.setStatus("current")
_DLldpExtLldpForward_Type = TruthValue
_DLldpExtLldpForward_Object = MibScalar
dLldpExtLldpForward = _DLldpExtLldpForward_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 2),
    _DLldpExtLldpForward_Type()
)
dLldpExtLldpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtLldpForward.setStatus("current")
_DLldpExtLldpTrapEnabled_Type = TruthValue
_DLldpExtLldpTrapEnabled_Object = MibScalar
dLldpExtLldpTrapEnabled = _DLldpExtLldpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 3),
    _DLldpExtLldpTrapEnabled_Type()
)
dLldpExtLldpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtLldpTrapEnabled.setStatus("current")
_DLldpExtLldpMedTrapEnabled_Type = TruthValue
_DLldpExtLldpMedTrapEnabled_Object = MibScalar
dLldpExtLldpMedTrapEnabled = _DLldpExtLldpMedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 4),
    _DLldpExtLldpMedTrapEnabled_Type()
)
dLldpExtLldpMedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtLldpMedTrapEnabled.setStatus("current")
_DLldpExtClearStats_ObjectIdentity = ObjectIdentity
dLldpExtClearStats = _DLldpExtClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5)
)


class _DLldpExtClearGlobalStats_Type(Integer32):
    """Custom type dLldpExtClearGlobalStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DLldpExtClearGlobalStats_Type.__name__ = "Integer32"
_DLldpExtClearGlobalStats_Object = MibScalar
dLldpExtClearGlobalStats = _DLldpExtClearGlobalStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5, 1),
    _DLldpExtClearGlobalStats_Type()
)
dLldpExtClearGlobalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtClearGlobalStats.setStatus("current")


class _DLldpExtClearAllPortsStats_Type(Integer32):
    """Custom type dLldpExtClearAllPortsStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DLldpExtClearAllPortsStats_Type.__name__ = "Integer32"
_DLldpExtClearAllPortsStats_Object = MibScalar
dLldpExtClearAllPortsStats = _DLldpExtClearAllPortsStats_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5, 2),
    _DLldpExtClearAllPortsStats_Type()
)
dLldpExtClearAllPortsStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtClearAllPortsStats.setStatus("current")


class _DLldpExtClearCounterByPort_Type(Integer32):
    """Custom type dLldpExtClearCounterByPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_DLldpExtClearCounterByPort_Type.__name__ = "Integer32"
_DLldpExtClearCounterByPort_Object = MibScalar
dLldpExtClearCounterByPort = _DLldpExtClearCounterByPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5, 3),
    _DLldpExtClearCounterByPort_Type()
)
dLldpExtClearCounterByPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtClearCounterByPort.setStatus("current")


class _DLldpExtClearAllNeighbors_Type(Integer32):
    """Custom type dLldpExtClearAllNeighbors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DLldpExtClearAllNeighbors_Type.__name__ = "Integer32"
_DLldpExtClearAllNeighbors_Object = MibScalar
dLldpExtClearAllNeighbors = _DLldpExtClearAllNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5, 4),
    _DLldpExtClearAllNeighbors_Type()
)
dLldpExtClearAllNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtClearAllNeighbors.setStatus("current")


class _DLldpExtClearNeighborsByPort_Type(Integer32):
    """Custom type dLldpExtClearNeighborsByPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_DLldpExtClearNeighborsByPort_Type.__name__ = "Integer32"
_DLldpExtClearNeighborsByPort_Object = MibScalar
dLldpExtClearNeighborsByPort = _DLldpExtClearNeighborsByPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 5, 5),
    _DLldpExtClearNeighborsByPort_Type()
)
dLldpExtClearNeighborsByPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtClearNeighborsByPort.setStatus("current")
_DLldpExtPortSubTypeTable_Object = MibTable
dLldpExtPortSubTypeTable = _DLldpExtPortSubTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 6)
)
if mibBuilder.loadTexts:
    dLldpExtPortSubTypeTable.setStatus("current")
_DLldpExtPortSubTypeEntry_Object = MibTableRow
dLldpExtPortSubTypeEntry = _DLldpExtPortSubTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 6, 1)
)
dLldpExtPortSubTypeEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    dLldpExtPortSubTypeEntry.setStatus("current")


class _DLldpExtPortSubType_Type(Integer32):
    """Custom type dLldpExtPortSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localPortNumber", 1),
          ("macAddress", 2))
    )


_DLldpExtPortSubType_Type.__name__ = "Integer32"
_DLldpExtPortSubType_Object = MibTableColumn
dLldpExtPortSubType = _DLldpExtPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 1, 6, 1, 1),
    _DLldpExtPortSubType_Type()
)
dLldpExtPortSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLldpExtPortSubType.setStatus("current")
_DLldpExtMIBConformance_ObjectIdentity = ObjectIdentity
dLldpExtMIBConformance = _DLldpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2)
)
_DLldpExtMIBCompliances_ObjectIdentity = ObjectIdentity
dLldpExtMIBCompliances = _DLldpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 1)
)
_DLldpExtMIBGroups_ObjectIdentity = ObjectIdentity
dLldpExtMIBGroups = _DLldpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 2)
)

# Managed Objects groups

dLldpExtBasicCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 2, 1)
)
dLldpExtBasicCfgGroup.setObjects(
      *(("DLINKSW-LLDP-EXT-MIB", "dLldpExtLldpEnabled"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtLldpForward"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtLldpTrapEnabled"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtLldpMedTrapEnabled"))
)
if mibBuilder.loadTexts:
    dLldpExtBasicCfgGroup.setStatus("current")

dLldpExtClearStatsCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 2, 2)
)
dLldpExtClearStatsCounterGroup.setObjects(
      *(("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearGlobalStats"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearAllPortsStats"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearCounterByPort"))
)
if mibBuilder.loadTexts:
    dLldpExtClearStatsCounterGroup.setStatus("current")

dLldpExtClearNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 2, 3)
)
dLldpExtClearNeighborGroup.setObjects(
      *(("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearAllNeighbors"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearNeighborsByPort"))
)
if mibBuilder.loadTexts:
    dLldpExtClearNeighborGroup.setStatus("current")

dLldpExtPortSubtypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 2, 4)
)
dLldpExtPortSubtypeGroup.setObjects(
    ("DLINKSW-LLDP-EXT-MIB", "dLldpExtPortSubType")
)
if mibBuilder.loadTexts:
    dLldpExtPortSubtypeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dLldpExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 20, 2, 1, 1)
)
dLldpExtMIBCompliance.setObjects(
      *(("DLINKSW-LLDP-EXT-MIB", "dLldpExtBasicCfgGroup"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearStatsCounterGroup"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtClearNeighborGroup"),
        ("DLINKSW-LLDP-EXT-MIB", "dLldpExtPortSubtypeGroup"))
)
if mibBuilder.loadTexts:
    dLldpExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-LLDP-EXT-MIB",
    **{"dlinkSwLldpExtMIB": dlinkSwLldpExtMIB,
       "dLldpExtMIBNotifications": dLldpExtMIBNotifications,
       "dLldpExtMIBObjects": dLldpExtMIBObjects,
       "dLldpExtLldpEnabled": dLldpExtLldpEnabled,
       "dLldpExtLldpForward": dLldpExtLldpForward,
       "dLldpExtLldpTrapEnabled": dLldpExtLldpTrapEnabled,
       "dLldpExtLldpMedTrapEnabled": dLldpExtLldpMedTrapEnabled,
       "dLldpExtClearStats": dLldpExtClearStats,
       "dLldpExtClearGlobalStats": dLldpExtClearGlobalStats,
       "dLldpExtClearAllPortsStats": dLldpExtClearAllPortsStats,
       "dLldpExtClearCounterByPort": dLldpExtClearCounterByPort,
       "dLldpExtClearAllNeighbors": dLldpExtClearAllNeighbors,
       "dLldpExtClearNeighborsByPort": dLldpExtClearNeighborsByPort,
       "dLldpExtPortSubTypeTable": dLldpExtPortSubTypeTable,
       "dLldpExtPortSubTypeEntry": dLldpExtPortSubTypeEntry,
       "dLldpExtPortSubType": dLldpExtPortSubType,
       "dLldpExtMIBConformance": dLldpExtMIBConformance,
       "dLldpExtMIBCompliances": dLldpExtMIBCompliances,
       "dLldpExtMIBCompliance": dLldpExtMIBCompliance,
       "dLldpExtMIBGroups": dLldpExtMIBGroups,
       "dLldpExtBasicCfgGroup": dLldpExtBasicCfgGroup,
       "dLldpExtClearStatsCounterGroup": dLldpExtClearStatsCounterGroup,
       "dLldpExtClearNeighborGroup": dLldpExtClearNeighborGroup,
       "dLldpExtPortSubtypeGroup": dLldpExtPortSubtypeGroup}
)
