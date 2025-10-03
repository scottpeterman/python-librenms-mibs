# SNMP MIB module (ARISTA-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arista\ARISTA-IF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:56 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

aristaIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15)
)
if mibBuilder.loadTexts:
    aristaIfMIB.setRevisions(
        ("2014-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaIf_ObjectIdentity = ObjectIdentity
aristaIf = _AristaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1)
)
_AristaIfTable_Object = MibTable
aristaIfTable = _AristaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1)
)
if mibBuilder.loadTexts:
    aristaIfTable.setStatus("current")
_AristaIfEntry_Object = MibTableRow
aristaIfEntry = _AristaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1)
)
aristaIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaIfEntry.setStatus("current")
_AristaIfCounterLastUpdated_Type = TimeTicks
_AristaIfCounterLastUpdated_Object = MibTableColumn
aristaIfCounterLastUpdated = _AristaIfCounterLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 1),
    _AristaIfCounterLastUpdated_Type()
)
aristaIfCounterLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfCounterLastUpdated.setStatus("current")
_AristaIfRateInterval_Type = TimeTicks
_AristaIfRateInterval_Object = MibTableColumn
aristaIfRateInterval = _AristaIfRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 2),
    _AristaIfRateInterval_Type()
)
aristaIfRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfRateInterval.setStatus("current")
_AristaIfInPktRate_Type = Gauge32
_AristaIfInPktRate_Object = MibTableColumn
aristaIfInPktRate = _AristaIfInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 3),
    _AristaIfInPktRate_Type()
)
aristaIfInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfInPktRate.setStatus("current")
_AristaIfOutPktRate_Type = Gauge32
_AristaIfOutPktRate_Object = MibTableColumn
aristaIfOutPktRate = _AristaIfOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 4),
    _AristaIfOutPktRate_Type()
)
aristaIfOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfOutPktRate.setStatus("current")
_AristaIfInOctetRate_Type = CounterBasedGauge64
_AristaIfInOctetRate_Object = MibTableColumn
aristaIfInOctetRate = _AristaIfInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 5),
    _AristaIfInOctetRate_Type()
)
aristaIfInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfInOctetRate.setStatus("current")
_AristaIfOutOctetRate_Type = CounterBasedGauge64
_AristaIfOutOctetRate_Object = MibTableColumn
aristaIfOutOctetRate = _AristaIfOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 6),
    _AristaIfOutOctetRate_Type()
)
aristaIfOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfOutOctetRate.setStatus("current")
_AristaIfRatesLastUpdated_Type = TimeTicks
_AristaIfRatesLastUpdated_Object = MibTableColumn
aristaIfRatesLastUpdated = _AristaIfRatesLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 7),
    _AristaIfRatesLastUpdated_Type()
)
aristaIfRatesLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfRatesLastUpdated.setStatus("current")
_AristaIfOperStatusChanges_Type = Counter32
_AristaIfOperStatusChanges_Object = MibTableColumn
aristaIfOperStatusChanges = _AristaIfOperStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 8),
    _AristaIfOperStatusChanges_Type()
)
aristaIfOperStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfOperStatusChanges.setStatus("current")
_AristaIfInAclDrops_Type = Counter32
_AristaIfInAclDrops_Object = MibTableColumn
aristaIfInAclDrops = _AristaIfInAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 9),
    _AristaIfInAclDrops_Type()
)
aristaIfInAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIfInAclDrops.setStatus("current")
_AristaIfConformance_ObjectIdentity = ObjectIdentity
aristaIfConformance = _AristaIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 2)
)
_AristaIfGroups_ObjectIdentity = ObjectIdentity
aristaIfGroups = _AristaIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1)
)
_AristaIfCompliances_ObjectIdentity = ObjectIdentity
aristaIfCompliances = _AristaIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2)
)

# Managed Objects groups

aristaIfAdditionalInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1, 1)
)
aristaIfAdditionalInformationGroup.setObjects(
      *(("ARISTA-IF-MIB", "aristaIfCounterLastUpdated"),
        ("ARISTA-IF-MIB", "aristaIfRateInterval"),
        ("ARISTA-IF-MIB", "aristaIfInPktRate"),
        ("ARISTA-IF-MIB", "aristaIfOutPktRate"),
        ("ARISTA-IF-MIB", "aristaIfInOctetRate"),
        ("ARISTA-IF-MIB", "aristaIfOutOctetRate"),
        ("ARISTA-IF-MIB", "aristaIfRatesLastUpdated"),
        ("ARISTA-IF-MIB", "aristaIfOperStatusChanges"),
        ("ARISTA-IF-MIB", "aristaIfInAclDrops"))
)
if mibBuilder.loadTexts:
    aristaIfAdditionalInformationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2, 1)
)
aristaIfCompliance.setObjects(
    ("ARISTA-IF-MIB", "aristaIfAdditionalInformationGroup")
)
if mibBuilder.loadTexts:
    aristaIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-IF-MIB",
    **{"aristaIfMIB": aristaIfMIB,
       "aristaIf": aristaIf,
       "aristaIfTable": aristaIfTable,
       "aristaIfEntry": aristaIfEntry,
       "aristaIfCounterLastUpdated": aristaIfCounterLastUpdated,
       "aristaIfRateInterval": aristaIfRateInterval,
       "aristaIfInPktRate": aristaIfInPktRate,
       "aristaIfOutPktRate": aristaIfOutPktRate,
       "aristaIfInOctetRate": aristaIfInOctetRate,
       "aristaIfOutOctetRate": aristaIfOutOctetRate,
       "aristaIfRatesLastUpdated": aristaIfRatesLastUpdated,
       "aristaIfOperStatusChanges": aristaIfOperStatusChanges,
       "aristaIfInAclDrops": aristaIfInAclDrops,
       "aristaIfConformance": aristaIfConformance,
       "aristaIfGroups": aristaIfGroups,
       "aristaIfAdditionalInformationGroup": aristaIfAdditionalInformationGroup,
       "aristaIfCompliances": aristaIfCompliances,
       "aristaIfCompliance": aristaIfCompliance}
)
