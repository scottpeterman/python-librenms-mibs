# SNMP MIB module (OCCAM-ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-ETHERLIKE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:23 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(occamGenericEtherlikeModules,
 occamGenericInterfaceModules) = mibBuilder.importSymbols(
    "OCCAM-REG-MODULE",
    "occamGenericEtherlikeModules",
    "occamGenericInterfaceModules")

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
 enterprises,
 iso,
 mib_2,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

etherMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etherMIB.setRevisions(
        ("2001-04-27 10:51",
         "1999-08-24 04:00",
         "1998-06-03 21:50",
         "1994-02-03 04:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_EtherMIBObjects_ObjectIdentity = ObjectIdentity
etherMIBObjects = _EtherMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1)
)
_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7)
)
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("current")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "OCCAM-ETHERLIKE-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("current")
_Dot3StatsIndex_Type = InterfaceIndex
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("current")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
_Dot3Tests_ObjectIdentity = ObjectIdentity
dot3Tests = _Dot3Tests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 6)
)
_Dot3Errors_ObjectIdentity = ObjectIdentity
dot3Errors = _Dot3Errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 1, 7, 7)
)
_EtherConformance_ObjectIdentity = ObjectIdentity
etherConformance = _EtherConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 2)
)
_EtherGroups_ObjectIdentity = ObjectIdentity
etherGroups = _EtherGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 2, 1)
)
_EtherCompliances_ObjectIdentity = ObjectIdentity
etherCompliances = _EtherCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-ETHERLIKE-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "mgmt": mgmt,
       "etherMIB": etherMIB,
       "etherMIBObjects": etherMIBObjects,
       "dot3": dot3,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3Tests": dot3Tests,
       "dot3Errors": dot3Errors,
       "etherConformance": etherConformance,
       "etherGroups": etherGroups,
       "etherCompliances": etherCompliances}
)
