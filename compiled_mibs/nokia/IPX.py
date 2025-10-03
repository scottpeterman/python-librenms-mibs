# SNMP MIB module (IPX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\IPX
# Produced by pysmi-1.6.2 at Thu Oct  2 12:16:34 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5)
)
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1)
)
_IpxBasicSysTable_Object = MibTable
ipxBasicSysTable = _IpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ipxBasicSysTable.setStatus("current")
_IpxBasicSysEntry_Object = MibTableRow
ipxBasicSysEntry = _IpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1)
)
ipxBasicSysEntry.setIndexNames(
    (0, "IPX", "ipxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    ipxBasicSysEntry.setStatus("current")
_IpxBasicSysInstance_Type = Integer32
_IpxBasicSysInstance_Object = MibTableColumn
ipxBasicSysInstance = _IpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 1),
    _IpxBasicSysInstance_Type()
)
ipxBasicSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysInstance.setStatus("current")


class _IpxBasicSysExistState_Type(Integer32):
    """Custom type ipxBasicSysExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxBasicSysExistState_Type.__name__ = "Integer32"
_IpxBasicSysExistState_Object = MibTableColumn
ipxBasicSysExistState = _IpxBasicSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 2),
    _IpxBasicSysExistState_Type()
)
ipxBasicSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysExistState.setStatus("current")
_IpxBasicSysNetNumber_Type = NetNumber
_IpxBasicSysNetNumber_Object = MibTableColumn
ipxBasicSysNetNumber = _IpxBasicSysNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 3),
    _IpxBasicSysNetNumber_Type()
)
ipxBasicSysNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNetNumber.setStatus("current")


class _IpxBasicSysNode_Type(OctetString):
    """Custom type ipxBasicSysNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxBasicSysNode_Type.__name__ = "OctetString"
_IpxBasicSysNode_Object = MibTableColumn
ipxBasicSysNode = _IpxBasicSysNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 4),
    _IpxBasicSysNode_Type()
)
ipxBasicSysNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNode.setStatus("current")


class _IpxBasicSysName_Type(OctetString):
    """Custom type ipxBasicSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxBasicSysName_Type.__name__ = "OctetString"
_IpxBasicSysName_Object = MibTableColumn
ipxBasicSysName = _IpxBasicSysName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 5),
    _IpxBasicSysName_Type()
)
ipxBasicSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysName.setStatus("current")
_IpxBasicSysInReceives_Type = Counter32
_IpxBasicSysInReceives_Object = MibTableColumn
ipxBasicSysInReceives = _IpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 6),
    _IpxBasicSysInReceives_Type()
)
ipxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInReceives.setStatus("current")
_IpxBasicSysInHdrErrors_Type = Counter32
_IpxBasicSysInHdrErrors_Object = MibTableColumn
ipxBasicSysInHdrErrors = _IpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 7),
    _IpxBasicSysInHdrErrors_Type()
)
ipxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInHdrErrors.setStatus("current")
_IpxBasicSysInUnknownSockets_Type = Counter32
_IpxBasicSysInUnknownSockets_Object = MibTableColumn
ipxBasicSysInUnknownSockets = _IpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 8),
    _IpxBasicSysInUnknownSockets_Type()
)
ipxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInUnknownSockets.setStatus("current")
_IpxBasicSysInDiscards_Type = Counter32
_IpxBasicSysInDiscards_Object = MibTableColumn
ipxBasicSysInDiscards = _IpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 9),
    _IpxBasicSysInDiscards_Type()
)
ipxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDiscards.setStatus("current")
_IpxBasicSysInBadChecksums_Type = Counter32
_IpxBasicSysInBadChecksums_Object = MibTableColumn
ipxBasicSysInBadChecksums = _IpxBasicSysInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 10),
    _IpxBasicSysInBadChecksums_Type()
)
ipxBasicSysInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInBadChecksums.setStatus("current")
_IpxBasicSysInDelivers_Type = Counter32
_IpxBasicSysInDelivers_Object = MibTableColumn
ipxBasicSysInDelivers = _IpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 11),
    _IpxBasicSysInDelivers_Type()
)
ipxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDelivers.setStatus("current")
_IpxBasicSysNoRoutes_Type = Counter32
_IpxBasicSysNoRoutes_Object = MibTableColumn
ipxBasicSysNoRoutes = _IpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 12),
    _IpxBasicSysNoRoutes_Type()
)
ipxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysNoRoutes.setStatus("current")
_IpxBasicSysOutRequests_Type = Counter32
_IpxBasicSysOutRequests_Object = MibTableColumn
ipxBasicSysOutRequests = _IpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 13),
    _IpxBasicSysOutRequests_Type()
)
ipxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutRequests.setStatus("current")
_IpxBasicSysOutMalformedRequests_Type = Counter32
_IpxBasicSysOutMalformedRequests_Object = MibTableColumn
ipxBasicSysOutMalformedRequests = _IpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 14),
    _IpxBasicSysOutMalformedRequests_Type()
)
ipxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutMalformedRequests.setStatus("current")
_IpxBasicSysOutDiscards_Type = Counter32
_IpxBasicSysOutDiscards_Object = MibTableColumn
ipxBasicSysOutDiscards = _IpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 15),
    _IpxBasicSysOutDiscards_Type()
)
ipxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutDiscards.setStatus("current")
_IpxBasicSysOutPackets_Type = Counter32
_IpxBasicSysOutPackets_Object = MibTableColumn
ipxBasicSysOutPackets = _IpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 16),
    _IpxBasicSysOutPackets_Type()
)
ipxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutPackets.setStatus("current")
_IpxBasicSysConfigSockets_Type = Integer32
_IpxBasicSysConfigSockets_Object = MibTableColumn
ipxBasicSysConfigSockets = _IpxBasicSysConfigSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 17),
    _IpxBasicSysConfigSockets_Type()
)
ipxBasicSysConfigSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysConfigSockets.setStatus("current")
_IpxBasicSysOpenSocketFails_Type = Counter32
_IpxBasicSysOpenSocketFails_Object = MibTableColumn
ipxBasicSysOpenSocketFails = _IpxBasicSysOpenSocketFails_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 18),
    _IpxBasicSysOpenSocketFails_Type()
)
ipxBasicSysOpenSocketFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOpenSocketFails.setStatus("current")
_IpxAdvSysTable_Object = MibTable
ipxAdvSysTable = _IpxAdvSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ipxAdvSysTable.setStatus("current")
_IpxAdvSysEntry_Object = MibTableRow
ipxAdvSysEntry = _IpxAdvSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1)
)
ipxAdvSysEntry.setIndexNames(
    (0, "IPX", "ipxAdvSysInstance"),
)
if mibBuilder.loadTexts:
    ipxAdvSysEntry.setStatus("current")
_IpxAdvSysInstance_Type = Integer32
_IpxAdvSysInstance_Object = MibTableColumn
ipxAdvSysInstance = _IpxAdvSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 1),
    _IpxAdvSysInstance_Type()
)
ipxAdvSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysInstance.setStatus("current")


class _IpxAdvSysMaxPathSplits_Type(Integer32):
    """Custom type ipxAdvSysMaxPathSplits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpxAdvSysMaxPathSplits_Type.__name__ = "Integer32"
_IpxAdvSysMaxPathSplits_Object = MibTableColumn
ipxAdvSysMaxPathSplits = _IpxAdvSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 2),
    _IpxAdvSysMaxPathSplits_Type()
)
ipxAdvSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxPathSplits.setStatus("current")


class _IpxAdvSysMaxHops_Type(Integer32):
    """Custom type ipxAdvSysMaxHops based on Integer32"""
    defaultValue = 64


_IpxAdvSysMaxHops_Type.__name__ = "Integer32"
_IpxAdvSysMaxHops_Object = MibTableColumn
ipxAdvSysMaxHops = _IpxAdvSysMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 3),
    _IpxAdvSysMaxHops_Type()
)
ipxAdvSysMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxHops.setStatus("current")
_IpxAdvSysInTooManyHops_Type = Counter32
_IpxAdvSysInTooManyHops_Object = MibTableColumn
ipxAdvSysInTooManyHops = _IpxAdvSysInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 4),
    _IpxAdvSysInTooManyHops_Type()
)
ipxAdvSysInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysInTooManyHops.setStatus("current")
_IpxAdvSysInFiltered_Type = Counter32
_IpxAdvSysInFiltered_Object = MibTableColumn
ipxAdvSysInFiltered = _IpxAdvSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 5),
    _IpxAdvSysInFiltered_Type()
)
ipxAdvSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysInFiltered.setStatus("current")
_IpxAdvSysInCompressDiscards_Type = Counter32
_IpxAdvSysInCompressDiscards_Object = MibTableColumn
ipxAdvSysInCompressDiscards = _IpxAdvSysInCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 6),
    _IpxAdvSysInCompressDiscards_Type()
)
ipxAdvSysInCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysInCompressDiscards.setStatus("current")
_IpxAdvSysNETBIOSPackets_Type = Counter32
_IpxAdvSysNETBIOSPackets_Object = MibTableColumn
ipxAdvSysNETBIOSPackets = _IpxAdvSysNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 7),
    _IpxAdvSysNETBIOSPackets_Type()
)
ipxAdvSysNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysNETBIOSPackets.setStatus("current")
_IpxAdvSysForwPackets_Type = Counter32
_IpxAdvSysForwPackets_Object = MibTableColumn
ipxAdvSysForwPackets = _IpxAdvSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 8),
    _IpxAdvSysForwPackets_Type()
)
ipxAdvSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysForwPackets.setStatus("current")
_IpxAdvSysOutFiltered_Type = Counter32
_IpxAdvSysOutFiltered_Object = MibTableColumn
ipxAdvSysOutFiltered = _IpxAdvSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 9),
    _IpxAdvSysOutFiltered_Type()
)
ipxAdvSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutFiltered.setStatus("current")
_IpxAdvSysOutCompressDiscards_Type = Counter32
_IpxAdvSysOutCompressDiscards_Object = MibTableColumn
ipxAdvSysOutCompressDiscards = _IpxAdvSysOutCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 10),
    _IpxAdvSysOutCompressDiscards_Type()
)
ipxAdvSysOutCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutCompressDiscards.setStatus("current")
_IpxAdvSysCircCount_Type = Integer32
_IpxAdvSysCircCount_Object = MibTableColumn
ipxAdvSysCircCount = _IpxAdvSysCircCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 11),
    _IpxAdvSysCircCount_Type()
)
ipxAdvSysCircCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysCircCount.setStatus("current")
_IpxAdvSysDestCount_Type = Integer32
_IpxAdvSysDestCount_Object = MibTableColumn
ipxAdvSysDestCount = _IpxAdvSysDestCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 12),
    _IpxAdvSysDestCount_Type()
)
ipxAdvSysDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysDestCount.setStatus("current")
_IpxAdvSysServCount_Type = Integer32
_IpxAdvSysServCount_Object = MibTableColumn
ipxAdvSysServCount = _IpxAdvSysServCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 13),
    _IpxAdvSysServCount_Type()
)
ipxAdvSysServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysServCount.setStatus("current")
_IpxCircuit_ObjectIdentity = ObjectIdentity
ipxCircuit = _IpxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("current")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "IPX", "ipxCircSysInstance"),
    (0, "IPX", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("current")
_IpxCircSysInstance_Type = Integer32
_IpxCircSysInstance_Object = MibTableColumn
ipxCircSysInstance = _IpxCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 1),
    _IpxCircSysInstance_Type()
)
ipxCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSysInstance.setStatus("current")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 2),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("current")


class _IpxCircExistState_Type(Integer32):
    """Custom type ipxCircExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxCircExistState_Type.__name__ = "Integer32"
_IpxCircExistState_Object = MibTableColumn
ipxCircExistState = _IpxCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 3),
    _IpxCircExistState_Type()
)
ipxCircExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircExistState.setStatus("current")


class _IpxCircOperState_Type(Integer32):
    """Custom type ipxCircOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("sleeping", 3))
    )


_IpxCircOperState_Type.__name__ = "Integer32"
_IpxCircOperState_Object = MibTableColumn
ipxCircOperState = _IpxCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 4),
    _IpxCircOperState_Type()
)
ipxCircOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircOperState.setStatus("current")
_IpxCircIfIndex_Type = Integer32
_IpxCircIfIndex_Object = MibTableColumn
ipxCircIfIndex = _IpxCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 5),
    _IpxCircIfIndex_Type()
)
ipxCircIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIfIndex.setStatus("current")


class _IpxCircName_Type(OctetString):
    """Custom type ipxCircName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxCircName_Type.__name__ = "OctetString"
_IpxCircName_Object = MibTableColumn
ipxCircName = _IpxCircName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 6),
    _IpxCircName_Type()
)
ipxCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircName.setStatus("current")


class _IpxCircType_Type(Integer32):
    """Custom type ipxCircType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("broadcast", 2),
          ("ptToPt", 3),
          ("wanRIP", 4),
          ("unnumberedRIP", 5),
          ("dynamic", 6),
          ("wanWS", 7))
    )


_IpxCircType_Type.__name__ = "Integer32"
_IpxCircType_Object = MibTableColumn
ipxCircType = _IpxCircType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 7),
    _IpxCircType_Type()
)
ipxCircType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircType.setStatus("current")


class _IpxCircDialName_Type(OctetString):
    """Custom type ipxCircDialName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxCircDialName_Type.__name__ = "OctetString"
_IpxCircDialName_Object = MibTableColumn
ipxCircDialName = _IpxCircDialName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 8),
    _IpxCircDialName_Type()
)
ipxCircDialName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircDialName.setStatus("current")
_IpxCircLocalMaxPacketSize_Type = Integer32
_IpxCircLocalMaxPacketSize_Object = MibTableColumn
ipxCircLocalMaxPacketSize = _IpxCircLocalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 9),
    _IpxCircLocalMaxPacketSize_Type()
)
ipxCircLocalMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircLocalMaxPacketSize.setStatus("current")


class _IpxCircCompressState_Type(Integer32):
    """Custom type ipxCircCompressState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxCircCompressState_Type.__name__ = "Integer32"
_IpxCircCompressState_Object = MibTableColumn
ipxCircCompressState = _IpxCircCompressState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 10),
    _IpxCircCompressState_Type()
)
ipxCircCompressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircCompressState.setStatus("current")


class _IpxCircCompressSlots_Type(Integer32):
    """Custom type ipxCircCompressSlots based on Integer32"""
    defaultValue = 16


_IpxCircCompressSlots_Type.__name__ = "Integer32"
_IpxCircCompressSlots_Object = MibTableColumn
ipxCircCompressSlots = _IpxCircCompressSlots_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 11),
    _IpxCircCompressSlots_Type()
)
ipxCircCompressSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircCompressSlots.setStatus("current")


class _IpxCircStaticStatus_Type(Integer32):
    """Custom type ipxCircStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("current", 2),
          ("changed", 3),
          ("read", 4),
          ("reading", 5),
          ("write", 6),
          ("writing", 7))
    )


_IpxCircStaticStatus_Type.__name__ = "Integer32"
_IpxCircStaticStatus_Object = MibTableColumn
ipxCircStaticStatus = _IpxCircStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 12),
    _IpxCircStaticStatus_Type()
)
ipxCircStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircStaticStatus.setStatus("current")
_IpxCircCompressedSent_Type = Counter32
_IpxCircCompressedSent_Object = MibTableColumn
ipxCircCompressedSent = _IpxCircCompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 13),
    _IpxCircCompressedSent_Type()
)
ipxCircCompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedSent.setStatus("current")
_IpxCircCompressedInitSent_Type = Counter32
_IpxCircCompressedInitSent_Object = MibTableColumn
ipxCircCompressedInitSent = _IpxCircCompressedInitSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 14),
    _IpxCircCompressedInitSent_Type()
)
ipxCircCompressedInitSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedInitSent.setStatus("current")
_IpxCircCompressedRejectsSent_Type = Counter32
_IpxCircCompressedRejectsSent_Object = MibTableColumn
ipxCircCompressedRejectsSent = _IpxCircCompressedRejectsSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 15),
    _IpxCircCompressedRejectsSent_Type()
)
ipxCircCompressedRejectsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedRejectsSent.setStatus("current")
_IpxCircUncompressedSent_Type = Counter32
_IpxCircUncompressedSent_Object = MibTableColumn
ipxCircUncompressedSent = _IpxCircUncompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 16),
    _IpxCircUncompressedSent_Type()
)
ipxCircUncompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircUncompressedSent.setStatus("current")
_IpxCircCompressedReceived_Type = Counter32
_IpxCircCompressedReceived_Object = MibTableColumn
ipxCircCompressedReceived = _IpxCircCompressedReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 17),
    _IpxCircCompressedReceived_Type()
)
ipxCircCompressedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedReceived.setStatus("current")
_IpxCircCompressedInitReceived_Type = Counter32
_IpxCircCompressedInitReceived_Object = MibTableColumn
ipxCircCompressedInitReceived = _IpxCircCompressedInitReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 18),
    _IpxCircCompressedInitReceived_Type()
)
ipxCircCompressedInitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedInitReceived.setStatus("current")
_IpxCircCompressedRejectsReceived_Type = Counter32
_IpxCircCompressedRejectsReceived_Object = MibTableColumn
ipxCircCompressedRejectsReceived = _IpxCircCompressedRejectsReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 19),
    _IpxCircCompressedRejectsReceived_Type()
)
ipxCircCompressedRejectsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedRejectsReceived.setStatus("current")
_IpxCircUncompressedReceived_Type = Counter32
_IpxCircUncompressedReceived_Object = MibTableColumn
ipxCircUncompressedReceived = _IpxCircUncompressedReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 20),
    _IpxCircUncompressedReceived_Type()
)
ipxCircUncompressedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircUncompressedReceived.setStatus("current")


class _IpxCircMediaType_Type(OctetString):
    """Custom type ipxCircMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxCircMediaType_Type.__name__ = "OctetString"
_IpxCircMediaType_Object = MibTableColumn
ipxCircMediaType = _IpxCircMediaType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 21),
    _IpxCircMediaType_Type()
)
ipxCircMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircMediaType.setStatus("current")
_IpxCircNetNumber_Type = NetNumber
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 22),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("current")
_IpxCircStateChanges_Type = Counter32
_IpxCircStateChanges_Object = MibTableColumn
ipxCircStateChanges = _IpxCircStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 23),
    _IpxCircStateChanges_Type()
)
ipxCircStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircStateChanges.setStatus("current")
_IpxCircInitFails_Type = Counter32
_IpxCircInitFails_Object = MibTableColumn
ipxCircInitFails = _IpxCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 24),
    _IpxCircInitFails_Type()
)
ipxCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircInitFails.setStatus("current")
_IpxCircDelay_Type = Integer32
_IpxCircDelay_Object = MibTableColumn
ipxCircDelay = _IpxCircDelay_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 25),
    _IpxCircDelay_Type()
)
ipxCircDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircDelay.setStatus("current")
_IpxCircThroughput_Type = Integer32
_IpxCircThroughput_Object = MibTableColumn
ipxCircThroughput = _IpxCircThroughput_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 26),
    _IpxCircThroughput_Type()
)
ipxCircThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircThroughput.setStatus("current")


class _IpxCircNeighRouterName_Type(OctetString):
    """Custom type ipxCircNeighRouterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxCircNeighRouterName_Type.__name__ = "OctetString"
_IpxCircNeighRouterName_Object = MibTableColumn
ipxCircNeighRouterName = _IpxCircNeighRouterName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 27),
    _IpxCircNeighRouterName_Type()
)
ipxCircNeighRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircNeighRouterName.setStatus("current")
_IpxCircNeighInternalNetNum_Type = NetNumber
_IpxCircNeighInternalNetNum_Object = MibTableColumn
ipxCircNeighInternalNetNum = _IpxCircNeighInternalNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2, 1, 1, 28),
    _IpxCircNeighInternalNetNum_Type()
)
ipxCircNeighInternalNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircNeighInternalNetNum.setStatus("current")
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3)
)
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("current")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1)
)
ipxDestEntry.setIndexNames(
    (0, "IPX", "ipxDestSysInstance"),
    (0, "IPX", "ipxDestNetNum"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("current")
_IpxDestSysInstance_Type = Integer32
_IpxDestSysInstance_Object = MibTableColumn
ipxDestSysInstance = _IpxDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 1),
    _IpxDestSysInstance_Type()
)
ipxDestSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestSysInstance.setStatus("current")
_IpxDestNetNum_Type = NetNumber
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 2),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("current")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("rip", 3),
          ("nlsp", 4),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 3),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("current")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 4),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("current")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 5),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("current")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 6),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("current")
_IpxDestNextHopNICAddress_Type = PhysAddress
_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 7),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("current")
_IpxDestNextHopNetNum_Type = NetNumber
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 1, 1, 8),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("current")
_IpxStaticRouteTable_Object = MibTable
ipxStaticRouteTable = _IpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ipxStaticRouteTable.setStatus("current")
_IpxStaticRouteEntry_Object = MibTableRow
ipxStaticRouteEntry = _IpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1)
)
ipxStaticRouteEntry.setIndexNames(
    (0, "IPX", "ipxStaticRouteSysInstance"),
    (0, "IPX", "ipxStaticRouteCircIndex"),
    (0, "IPX", "ipxStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    ipxStaticRouteEntry.setStatus("current")
_IpxStaticRouteSysInstance_Type = Integer32
_IpxStaticRouteSysInstance_Object = MibTableColumn
ipxStaticRouteSysInstance = _IpxStaticRouteSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 1),
    _IpxStaticRouteSysInstance_Type()
)
ipxStaticRouteSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteSysInstance.setStatus("current")
_IpxStaticRouteCircIndex_Type = Integer32
_IpxStaticRouteCircIndex_Object = MibTableColumn
ipxStaticRouteCircIndex = _IpxStaticRouteCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 2),
    _IpxStaticRouteCircIndex_Type()
)
ipxStaticRouteCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteCircIndex.setStatus("current")
_IpxStaticRouteNetNum_Type = NetNumber
_IpxStaticRouteNetNum_Object = MibTableColumn
ipxStaticRouteNetNum = _IpxStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 3),
    _IpxStaticRouteNetNum_Type()
)
ipxStaticRouteNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteNetNum.setStatus("current")


class _IpxStaticRouteExistState_Type(Integer32):
    """Custom type ipxStaticRouteExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxStaticRouteExistState_Type.__name__ = "Integer32"
_IpxStaticRouteExistState_Object = MibTableColumn
ipxStaticRouteExistState = _IpxStaticRouteExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 4),
    _IpxStaticRouteExistState_Type()
)
ipxStaticRouteExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteExistState.setStatus("current")
_IpxStaticRouteTicks_Type = Integer32
_IpxStaticRouteTicks_Object = MibTableColumn
ipxStaticRouteTicks = _IpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 5),
    _IpxStaticRouteTicks_Type()
)
ipxStaticRouteTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteTicks.setStatus("current")
_IpxStaticRouteHopCount_Type = Integer32
_IpxStaticRouteHopCount_Object = MibTableColumn
ipxStaticRouteHopCount = _IpxStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3, 2, 1, 6),
    _IpxStaticRouteHopCount_Type()
)
ipxStaticRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticRouteHopCount.setStatus("current")
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4)
)
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("current")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1)
)
ipxServEntry.setIndexNames(
    (0, "IPX", "ipxServSysInstance"),
    (0, "IPX", "ipxServType"),
    (0, "IPX", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("current")
_IpxServSysInstance_Type = Integer32
_IpxServSysInstance_Object = MibTableColumn
ipxServSysInstance = _IpxServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 1),
    _IpxServSysInstance_Type()
)
ipxServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServSysInstance.setStatus("current")


class _IpxServType_Type(OctetString):
    """Custom type ipxServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxServType_Type.__name__ = "OctetString"
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 2),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServType.setStatus("current")


class _IpxServName_Type(OctetString):
    """Custom type ipxServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "OctetString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 3),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServName.setStatus("current")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("nlsp", 4),
          ("static", 5),
          ("sap", 6))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 4),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("current")
_IpxServNetNum_Type = NetNumber
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 5),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("current")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 6),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("current")


class _IpxServSocket_Type(OctetString):
    """Custom type ipxServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxServSocket_Type.__name__ = "OctetString"
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 7),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("current")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 1, 1, 8),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("current")
_IpxDestServTable_Object = MibTable
ipxDestServTable = _IpxDestServTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    ipxDestServTable.setStatus("current")
_IpxDestServEntry_Object = MibTableRow
ipxDestServEntry = _IpxDestServEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1)
)
ipxDestServEntry.setIndexNames(
    (0, "IPX", "ipxDestServSysInstance"),
    (0, "IPX", "ipxDestServNetNum"),
    (0, "IPX", "ipxDestServNode"),
    (0, "IPX", "ipxDestServSocket"),
    (0, "IPX", "ipxDestServName"),
    (0, "IPX", "ipxDestServType"),
)
if mibBuilder.loadTexts:
    ipxDestServEntry.setStatus("current")
_IpxDestServSysInstance_Type = Integer32
_IpxDestServSysInstance_Object = MibTableColumn
ipxDestServSysInstance = _IpxDestServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 1),
    _IpxDestServSysInstance_Type()
)
ipxDestServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServSysInstance.setStatus("current")
_IpxDestServNetNum_Type = NetNumber
_IpxDestServNetNum_Object = MibTableColumn
ipxDestServNetNum = _IpxDestServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 2),
    _IpxDestServNetNum_Type()
)
ipxDestServNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServNetNum.setStatus("current")


class _IpxDestServNode_Type(OctetString):
    """Custom type ipxDestServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxDestServNode_Type.__name__ = "OctetString"
_IpxDestServNode_Object = MibTableColumn
ipxDestServNode = _IpxDestServNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 3),
    _IpxDestServNode_Type()
)
ipxDestServNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServNode.setStatus("current")


class _IpxDestServSocket_Type(OctetString):
    """Custom type ipxDestServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxDestServSocket_Type.__name__ = "OctetString"
_IpxDestServSocket_Object = MibTableColumn
ipxDestServSocket = _IpxDestServSocket_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 4),
    _IpxDestServSocket_Type()
)
ipxDestServSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServSocket.setStatus("current")


class _IpxDestServName_Type(OctetString):
    """Custom type ipxDestServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxDestServName_Type.__name__ = "OctetString"
_IpxDestServName_Object = MibTableColumn
ipxDestServName = _IpxDestServName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 5),
    _IpxDestServName_Type()
)
ipxDestServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServName.setStatus("current")


class _IpxDestServType_Type(OctetString):
    """Custom type ipxDestServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxDestServType_Type.__name__ = "OctetString"
_IpxDestServType_Object = MibTableColumn
ipxDestServType = _IpxDestServType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 6),
    _IpxDestServType_Type()
)
ipxDestServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServType.setStatus("current")


class _IpxDestServProtocol_Type(Integer32):
    """Custom type ipxDestServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("nlsp", 4),
          ("static", 5),
          ("sap", 6))
    )


_IpxDestServProtocol_Type.__name__ = "Integer32"
_IpxDestServProtocol_Object = MibTableColumn
ipxDestServProtocol = _IpxDestServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 7),
    _IpxDestServProtocol_Type()
)
ipxDestServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServProtocol.setStatus("current")
_IpxDestServHopCount_Type = Integer32
_IpxDestServHopCount_Object = MibTableColumn
ipxDestServHopCount = _IpxDestServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 2, 1, 8),
    _IpxDestServHopCount_Type()
)
ipxDestServHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestServHopCount.setStatus("current")
_IpxStaticServTable_Object = MibTable
ipxStaticServTable = _IpxStaticServTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3)
)
if mibBuilder.loadTexts:
    ipxStaticServTable.setStatus("current")
_IpxStaticServEntry_Object = MibTableRow
ipxStaticServEntry = _IpxStaticServEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1)
)
ipxStaticServEntry.setIndexNames(
    (0, "IPX", "ipxStaticServSysInstance"),
    (0, "IPX", "ipxStaticServCircIndex"),
    (0, "IPX", "ipxStaticServName"),
    (0, "IPX", "ipxStaticServType"),
)
if mibBuilder.loadTexts:
    ipxStaticServEntry.setStatus("current")
_IpxStaticServSysInstance_Type = Integer32
_IpxStaticServSysInstance_Object = MibTableColumn
ipxStaticServSysInstance = _IpxStaticServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 1),
    _IpxStaticServSysInstance_Type()
)
ipxStaticServSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServSysInstance.setStatus("current")
_IpxStaticServCircIndex_Type = Integer32
_IpxStaticServCircIndex_Object = MibTableColumn
ipxStaticServCircIndex = _IpxStaticServCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 2),
    _IpxStaticServCircIndex_Type()
)
ipxStaticServCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServCircIndex.setStatus("current")


class _IpxStaticServName_Type(OctetString):
    """Custom type ipxStaticServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxStaticServName_Type.__name__ = "OctetString"
_IpxStaticServName_Object = MibTableColumn
ipxStaticServName = _IpxStaticServName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 3),
    _IpxStaticServName_Type()
)
ipxStaticServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServName.setStatus("current")


class _IpxStaticServType_Type(OctetString):
    """Custom type ipxStaticServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxStaticServType_Type.__name__ = "OctetString"
_IpxStaticServType_Object = MibTableColumn
ipxStaticServType = _IpxStaticServType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 4),
    _IpxStaticServType_Type()
)
ipxStaticServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServType.setStatus("current")


class _IpxStaticServExistState_Type(Integer32):
    """Custom type ipxStaticServExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxStaticServExistState_Type.__name__ = "Integer32"
_IpxStaticServExistState_Object = MibTableColumn
ipxStaticServExistState = _IpxStaticServExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 5),
    _IpxStaticServExistState_Type()
)
ipxStaticServExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServExistState.setStatus("current")
_IpxStaticServNetNum_Type = NetNumber
_IpxStaticServNetNum_Object = MibTableColumn
ipxStaticServNetNum = _IpxStaticServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 6),
    _IpxStaticServNetNum_Type()
)
ipxStaticServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServNetNum.setStatus("current")


class _IpxStaticServNode_Type(OctetString):
    """Custom type ipxStaticServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxStaticServNode_Type.__name__ = "OctetString"
_IpxStaticServNode_Object = MibTableColumn
ipxStaticServNode = _IpxStaticServNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 7),
    _IpxStaticServNode_Type()
)
ipxStaticServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServNode.setStatus("current")


class _IpxStaticServSocket_Type(OctetString):
    """Custom type ipxStaticServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxStaticServSocket_Type.__name__ = "OctetString"
_IpxStaticServSocket_Object = MibTableColumn
ipxStaticServSocket = _IpxStaticServSocket_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 8),
    _IpxStaticServSocket_Type()
)
ipxStaticServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServSocket.setStatus("current")
_IpxStaticServHopCount_Type = Integer32
_IpxStaticServHopCount_Object = MibTableColumn
ipxStaticServHopCount = _IpxStaticServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4, 3, 1, 9),
    _IpxStaticServHopCount_Type()
)
ipxStaticServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxStaticServHopCount.setStatus("current")
_IpxTraps_ObjectIdentity = ObjectIdentity
ipxTraps = _IpxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 5)
)

# Managed Objects groups


# Notification objects

ipxTrapCircuitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 5, 0, 1)
)
ipxTrapCircuitDown.setObjects(
      *(("IPX", "ipxCircSysInstance"),
        ("IPX", "ipxCircIndex"))
)
if mibBuilder.loadTexts:
    ipxTrapCircuitDown.setStatus(
        ""
    )

ipxTrapCircuitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 5, 0, 2)
)
ipxTrapCircuitUp.setObjects(
      *(("IPX", "ipxCircSysInstance"),
        ("IPX", "ipxCircIndex"))
)
if mibBuilder.loadTexts:
    ipxTrapCircuitUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPX",
    **{"NetNumber": NetNumber,
       "novell": novell,
       "mibDoc": mibDoc,
       "ipx": ipx,
       "ipxSystem": ipxSystem,
       "ipxBasicSysTable": ipxBasicSysTable,
       "ipxBasicSysEntry": ipxBasicSysEntry,
       "ipxBasicSysInstance": ipxBasicSysInstance,
       "ipxBasicSysExistState": ipxBasicSysExistState,
       "ipxBasicSysNetNumber": ipxBasicSysNetNumber,
       "ipxBasicSysNode": ipxBasicSysNode,
       "ipxBasicSysName": ipxBasicSysName,
       "ipxBasicSysInReceives": ipxBasicSysInReceives,
       "ipxBasicSysInHdrErrors": ipxBasicSysInHdrErrors,
       "ipxBasicSysInUnknownSockets": ipxBasicSysInUnknownSockets,
       "ipxBasicSysInDiscards": ipxBasicSysInDiscards,
       "ipxBasicSysInBadChecksums": ipxBasicSysInBadChecksums,
       "ipxBasicSysInDelivers": ipxBasicSysInDelivers,
       "ipxBasicSysNoRoutes": ipxBasicSysNoRoutes,
       "ipxBasicSysOutRequests": ipxBasicSysOutRequests,
       "ipxBasicSysOutMalformedRequests": ipxBasicSysOutMalformedRequests,
       "ipxBasicSysOutDiscards": ipxBasicSysOutDiscards,
       "ipxBasicSysOutPackets": ipxBasicSysOutPackets,
       "ipxBasicSysConfigSockets": ipxBasicSysConfigSockets,
       "ipxBasicSysOpenSocketFails": ipxBasicSysOpenSocketFails,
       "ipxAdvSysTable": ipxAdvSysTable,
       "ipxAdvSysEntry": ipxAdvSysEntry,
       "ipxAdvSysInstance": ipxAdvSysInstance,
       "ipxAdvSysMaxPathSplits": ipxAdvSysMaxPathSplits,
       "ipxAdvSysMaxHops": ipxAdvSysMaxHops,
       "ipxAdvSysInTooManyHops": ipxAdvSysInTooManyHops,
       "ipxAdvSysInFiltered": ipxAdvSysInFiltered,
       "ipxAdvSysInCompressDiscards": ipxAdvSysInCompressDiscards,
       "ipxAdvSysNETBIOSPackets": ipxAdvSysNETBIOSPackets,
       "ipxAdvSysForwPackets": ipxAdvSysForwPackets,
       "ipxAdvSysOutFiltered": ipxAdvSysOutFiltered,
       "ipxAdvSysOutCompressDiscards": ipxAdvSysOutCompressDiscards,
       "ipxAdvSysCircCount": ipxAdvSysCircCount,
       "ipxAdvSysDestCount": ipxAdvSysDestCount,
       "ipxAdvSysServCount": ipxAdvSysServCount,
       "ipxCircuit": ipxCircuit,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircSysInstance": ipxCircSysInstance,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircExistState": ipxCircExistState,
       "ipxCircOperState": ipxCircOperState,
       "ipxCircIfIndex": ipxCircIfIndex,
       "ipxCircName": ipxCircName,
       "ipxCircType": ipxCircType,
       "ipxCircDialName": ipxCircDialName,
       "ipxCircLocalMaxPacketSize": ipxCircLocalMaxPacketSize,
       "ipxCircCompressState": ipxCircCompressState,
       "ipxCircCompressSlots": ipxCircCompressSlots,
       "ipxCircStaticStatus": ipxCircStaticStatus,
       "ipxCircCompressedSent": ipxCircCompressedSent,
       "ipxCircCompressedInitSent": ipxCircCompressedInitSent,
       "ipxCircCompressedRejectsSent": ipxCircCompressedRejectsSent,
       "ipxCircUncompressedSent": ipxCircUncompressedSent,
       "ipxCircCompressedReceived": ipxCircCompressedReceived,
       "ipxCircCompressedInitReceived": ipxCircCompressedInitReceived,
       "ipxCircCompressedRejectsReceived": ipxCircCompressedRejectsReceived,
       "ipxCircUncompressedReceived": ipxCircUncompressedReceived,
       "ipxCircMediaType": ipxCircMediaType,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircStateChanges": ipxCircStateChanges,
       "ipxCircInitFails": ipxCircInitFails,
       "ipxCircDelay": ipxCircDelay,
       "ipxCircThroughput": ipxCircThroughput,
       "ipxCircNeighRouterName": ipxCircNeighRouterName,
       "ipxCircNeighInternalNetNum": ipxCircNeighInternalNetNum,
       "ipxForwarding": ipxForwarding,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestSysInstance": ipxDestSysInstance,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxStaticRouteTable": ipxStaticRouteTable,
       "ipxStaticRouteEntry": ipxStaticRouteEntry,
       "ipxStaticRouteSysInstance": ipxStaticRouteSysInstance,
       "ipxStaticRouteCircIndex": ipxStaticRouteCircIndex,
       "ipxStaticRouteNetNum": ipxStaticRouteNetNum,
       "ipxStaticRouteExistState": ipxStaticRouteExistState,
       "ipxStaticRouteTicks": ipxStaticRouteTicks,
       "ipxStaticRouteHopCount": ipxStaticRouteHopCount,
       "ipxServices": ipxServices,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServSysInstance": ipxServSysInstance,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxDestServTable": ipxDestServTable,
       "ipxDestServEntry": ipxDestServEntry,
       "ipxDestServSysInstance": ipxDestServSysInstance,
       "ipxDestServNetNum": ipxDestServNetNum,
       "ipxDestServNode": ipxDestServNode,
       "ipxDestServSocket": ipxDestServSocket,
       "ipxDestServName": ipxDestServName,
       "ipxDestServType": ipxDestServType,
       "ipxDestServProtocol": ipxDestServProtocol,
       "ipxDestServHopCount": ipxDestServHopCount,
       "ipxStaticServTable": ipxStaticServTable,
       "ipxStaticServEntry": ipxStaticServEntry,
       "ipxStaticServSysInstance": ipxStaticServSysInstance,
       "ipxStaticServCircIndex": ipxStaticServCircIndex,
       "ipxStaticServName": ipxStaticServName,
       "ipxStaticServType": ipxStaticServType,
       "ipxStaticServExistState": ipxStaticServExistState,
       "ipxStaticServNetNum": ipxStaticServNetNum,
       "ipxStaticServNode": ipxStaticServNode,
       "ipxStaticServSocket": ipxStaticServSocket,
       "ipxStaticServHopCount": ipxStaticServHopCount,
       "ipxTraps": ipxTraps,
       "ipxTrapCircuitDown": ipxTrapCircuitDown,
       "ipxTrapCircuitUp": ipxTrapCircuitUp}
)
