# SNMP MIB module (CTRON-PORTMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-PORTMAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:10 2025
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

(ctPortMap,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPortMap")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortMap_ObjectIdentity = ObjectIdentity
portMap = _PortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1)
)
_PortMapTable_Object = MibTable
portMapTable = _PortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    portMapTable.setStatus("mandatory")
_PortMapEntry_Object = MibTableRow
portMapEntry = _PortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1)
)
portMapEntry.setIndexNames(
    (0, "CTRON-PORTMAP-MIB", "portMapIndex"),
)
if mibBuilder.loadTexts:
    portMapEntry.setStatus("mandatory")
_PortMapIndex_Type = Integer32
_PortMapIndex_Object = MibTableColumn
portMapIndex = _PortMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 1),
    _PortMapIndex_Type()
)
portMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMapIndex.setStatus("mandatory")
_PortMapRepeater_Type = Integer32
_PortMapRepeater_Object = MibTableColumn
portMapRepeater = _PortMapRepeater_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 2),
    _PortMapRepeater_Type()
)
portMapRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMapRepeater.setStatus("mandatory")


class _PortMapCapability_Type(Integer32):
    """Custom type portMapCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PortMapCapability_Type.__name__ = "Integer32"
_PortMapCapability_Object = MibTableColumn
portMapCapability = _PortMapCapability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 3),
    _PortMapCapability_Type()
)
portMapCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMapCapability.setStatus("mandatory")


class _PortMapOperationalMode_Type(Integer32):
    """Custom type portMapOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PortMapOperationalMode_Type.__name__ = "Integer32"
_PortMapOperationalMode_Object = MibTableColumn
portMapOperationalMode = _PortMapOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 4),
    _PortMapOperationalMode_Type()
)
portMapOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMapOperationalMode.setStatus("mandatory")


class _PortMapLastSeenSrcAddr_Type(OctetString):
    """Custom type portMapLastSeenSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_PortMapLastSeenSrcAddr_Type.__name__ = "OctetString"
_PortMapLastSeenSrcAddr_Object = MibTableColumn
portMapLastSeenSrcAddr = _PortMapLastSeenSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 5),
    _PortMapLastSeenSrcAddr_Type()
)
portMapLastSeenSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMapLastSeenSrcAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-PORTMAP-MIB",
    **{"portMap": portMap,
       "portMapTable": portMapTable,
       "portMapEntry": portMapEntry,
       "portMapIndex": portMapIndex,
       "portMapRepeater": portMapRepeater,
       "portMapCapability": portMapCapability,
       "portMapOperationalMode": portMapOperationalMode,
       "portMapLastSeenSrcAddr": portMapLastSeenSrcAddr}
)
