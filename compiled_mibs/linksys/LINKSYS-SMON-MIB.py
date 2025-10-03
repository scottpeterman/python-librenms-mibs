# SNMP MIB module (LINKSYS-SMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-SMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:57 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84)
)
if mibBuilder.loadTexts:
    rlSmon.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CopyModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor-only", 1),
          ("network", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlPortCopyMibVersion_Type = Integer32
_RlPortCopyMibVersion_Object = MibScalar
rlPortCopyMibVersion = _RlPortCopyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 1),
    _RlPortCopyMibVersion_Type()
)
rlPortCopyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopyMibVersion.setStatus("current")


class _RlPortCopySupport_Type(Integer32):
    """Custom type rlPortCopySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_RlPortCopySupport_Type.__name__ = "Integer32"
_RlPortCopySupport_Object = MibScalar
rlPortCopySupport = _RlPortCopySupport_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 2),
    _RlPortCopySupport_Type()
)
rlPortCopySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopySupport.setStatus("current")
_RlPortCopyVlanTaggingTable_Object = MibTable
rlPortCopyVlanTaggingTable = _RlPortCopyVlanTaggingTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 3)
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingTable.setStatus("current")
_RlPortCopyVlanTaggingEntry_Object = MibTableRow
rlPortCopyVlanTaggingEntry = _RlPortCopyVlanTaggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 3, 1)
)
rlPortCopyVlanTaggingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingEntry.setStatus("current")


class _RlPortCopyVlanTagging_Type(TruthValue):
    """Custom type rlPortCopyVlanTagging based on TruthValue"""
    defaultValue = 1


_RlPortCopyVlanTagging_Type.__name__ = "TruthValue"
_RlPortCopyVlanTagging_Object = MibTableColumn
rlPortCopyVlanTagging = _RlPortCopyVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 3, 1, 1),
    _RlPortCopyVlanTagging_Type()
)
rlPortCopyVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopyVlanTagging.setStatus("current")
_RlPortCopyMode_Type = CopyModeType
_RlPortCopyMode_Object = MibScalar
rlPortCopyMode = _RlPortCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 4),
    _RlPortCopyMode_Type()
)
rlPortCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopyMode.setStatus("current")


class _RlPortCopySessionsEnabled_Type(TruthValue):
    """Custom type rlPortCopySessionsEnabled based on TruthValue"""
    defaultValue = 1


_RlPortCopySessionsEnabled_Type.__name__ = "TruthValue"
_RlPortCopySessionsEnabled_Object = MibScalar
rlPortCopySessionsEnabled = _RlPortCopySessionsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 84, 5),
    _RlPortCopySessionsEnabled_Type()
)
rlPortCopySessionsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopySessionsEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-SMON-MIB",
    **{"CopyModeType": CopyModeType,
       "rlSmon": rlSmon,
       "rlPortCopyMibVersion": rlPortCopyMibVersion,
       "rlPortCopySupport": rlPortCopySupport,
       "rlPortCopyVlanTaggingTable": rlPortCopyVlanTaggingTable,
       "rlPortCopyVlanTaggingEntry": rlPortCopyVlanTaggingEntry,
       "rlPortCopyVlanTagging": rlPortCopyVlanTagging,
       "rlPortCopyMode": rlPortCopyMode,
       "rlPortCopySessionsEnabled": rlPortCopySessionsEnabled}
)
