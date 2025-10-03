# SNMP MIB module (MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\MPLS-TE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:15:59 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 95)
)
if mibBuilder.loadTexts:
    mplsTeMIB.setRevisions(
        ("2000-07-14 12:00",
         "2000-05-26 12:00",
         "2000-03-03 12:00",
         "1999-07-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLSPID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class MplsBitRate(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsBurstSize(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MplsTunnelIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_MplsTeObjects_ObjectIdentity = ObjectIdentity
mplsTeObjects = _MplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 1)
)


class _MplsTunnelIndexNext_Type(Integer32):
    """Custom type mplsTunnelIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelIndexNext_Type.__name__ = "Integer32"
_MplsTunnelIndexNext_Object = MibScalar
mplsTunnelIndexNext = _MplsTunnelIndexNext_Object(
    (1, 3, 6, 1, 3, 95, 1, 1),
    _MplsTunnelIndexNext_Type()
)
mplsTunnelIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIndexNext.setStatus("current")
_MplsTunnelTable_Object = MibTable
mplsTunnelTable = _MplsTunnelTable_Object(
    (1, 3, 6, 1, 3, 95, 1, 2)
)
if mibBuilder.loadTexts:
    mplsTunnelTable.setStatus("current")
_MplsTunnelEntry_Object = MibTableRow
mplsTunnelEntry = _MplsTunnelEntry_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1)
)
mplsTunnelEntry.setIndexNames(
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
)
if mibBuilder.loadTexts:
    mplsTunnelEntry.setStatus("current")
_MplsTunnelIndex_Type = MplsTunnelIndex
_MplsTunnelIndex_Object = MibTableColumn
mplsTunnelIndex = _MplsTunnelIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 1),
    _MplsTunnelIndex_Type()
)
mplsTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mplsTunnelIndex.setStatus("current")
_MplsTunnelInstance_Type = MplsTunnelIndex
_MplsTunnelInstance_Object = MibTableColumn
mplsTunnelInstance = _MplsTunnelInstance_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 2),
    _MplsTunnelInstance_Type()
)
mplsTunnelInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mplsTunnelInstance.setStatus("current")


class _MplsTunnelIngressLSRId_Type(Unsigned32):
    """Custom type mplsTunnelIngressLSRId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsTunnelIngressLSRId_Type.__name__ = "Unsigned32"
_MplsTunnelIngressLSRId_Object = MibTableColumn
mplsTunnelIngressLSRId = _MplsTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 3),
    _MplsTunnelIngressLSRId_Type()
)
mplsTunnelIngressLSRId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mplsTunnelIngressLSRId.setStatus("current")
_MplsTunnelName_Type = DisplayString
_MplsTunnelName_Object = MibTableColumn
mplsTunnelName = _MplsTunnelName_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 4),
    _MplsTunnelName_Type()
)
mplsTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelName.setStatus("current")
_MplsTunnelDescr_Type = DisplayString
_MplsTunnelDescr_Object = MibTableColumn
mplsTunnelDescr = _MplsTunnelDescr_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 5),
    _MplsTunnelDescr_Type()
)
mplsTunnelDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDescr.setStatus("current")


class _MplsTunnelIsIf_Type(TruthValue):
    """Custom type mplsTunnelIsIf based on TruthValue"""
    defaultValue = 2


_MplsTunnelIsIf_Type.__name__ = "TruthValue"
_MplsTunnelIsIf_Object = MibTableColumn
mplsTunnelIsIf = _MplsTunnelIsIf_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 6),
    _MplsTunnelIsIf_Type()
)
mplsTunnelIsIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsIf.setStatus("current")
_MplsTunnelIfIndex_Type = InterfaceIndexOrZero
_MplsTunnelIfIndex_Object = MibTableColumn
mplsTunnelIfIndex = _MplsTunnelIfIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 7),
    _MplsTunnelIfIndex_Type()
)
mplsTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIfIndex.setStatus("current")
_MplsTunnelXCPointer_Type = RowPointer
_MplsTunnelXCPointer_Object = MibTableColumn
mplsTunnelXCPointer = _MplsTunnelXCPointer_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 8),
    _MplsTunnelXCPointer_Type()
)
mplsTunnelXCPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelXCPointer.setStatus("current")


class _MplsTunnelSignallingProto_Type(Integer32):
    """Custom type mplsTunnelSignallingProto based on Integer32"""
    defaultValue = 1

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
          ("rsvp", 2),
          ("crldp", 3),
          ("other", 4))
    )


_MplsTunnelSignallingProto_Type.__name__ = "Integer32"
_MplsTunnelSignallingProto_Object = MibTableColumn
mplsTunnelSignallingProto = _MplsTunnelSignallingProto_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 9),
    _MplsTunnelSignallingProto_Type()
)
mplsTunnelSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSignallingProto.setStatus("current")


class _MplsTunnelSetupPrio_Type(Integer32):
    """Custom type mplsTunnelSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelSetupPrio_Type.__name__ = "Integer32"
_MplsTunnelSetupPrio_Object = MibTableColumn
mplsTunnelSetupPrio = _MplsTunnelSetupPrio_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 10),
    _MplsTunnelSetupPrio_Type()
)
mplsTunnelSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSetupPrio.setStatus("current")


class _MplsTunnelHoldingPrio_Type(Integer32):
    """Custom type mplsTunnelHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelHoldingPrio_Type.__name__ = "Integer32"
_MplsTunnelHoldingPrio_Object = MibTableColumn
mplsTunnelHoldingPrio = _MplsTunnelHoldingPrio_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 11),
    _MplsTunnelHoldingPrio_Type()
)
mplsTunnelHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHoldingPrio.setStatus("current")


class _MplsTunnelSessionAttributes_Type(Bits):
    """Custom type mplsTunnelSessionAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("fastReroute", 0),
          ("mergingPermitted", 1),
          ("isPersistent", 2),
          ("localProtectionAvailable", 3),
          ("isPinned", 4))
    )

_MplsTunnelSessionAttributes_Type.__name__ = "Bits"
_MplsTunnelSessionAttributes_Object = MibTableColumn
mplsTunnelSessionAttributes = _MplsTunnelSessionAttributes_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 12),
    _MplsTunnelSessionAttributes_Type()
)
mplsTunnelSessionAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSessionAttributes.setStatus("current")


class _MplsTunnelOwner_Type(Integer32):
    """Custom type mplsTunnelOwner based on Integer32"""
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
        *(("admin", 1),
          ("rsvp", 2),
          ("crldp", 3),
          ("policyAgent", 4),
          ("other", 5))
    )


_MplsTunnelOwner_Type.__name__ = "Integer32"
_MplsTunnelOwner_Object = MibTableColumn
mplsTunnelOwner = _MplsTunnelOwner_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 13),
    _MplsTunnelOwner_Type()
)
mplsTunnelOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelOwner.setStatus("current")
_MplsTunnelLocalProtectInUse_Type = TruthValue
_MplsTunnelLocalProtectInUse_Object = MibTableColumn
mplsTunnelLocalProtectInUse = _MplsTunnelLocalProtectInUse_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 14),
    _MplsTunnelLocalProtectInUse_Type()
)
mplsTunnelLocalProtectInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLocalProtectInUse.setStatus("current")
_MplsTunnelResourcePointer_Type = RowPointer
_MplsTunnelResourcePointer_Object = MibTableColumn
mplsTunnelResourcePointer = _MplsTunnelResourcePointer_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 15),
    _MplsTunnelResourcePointer_Type()
)
mplsTunnelResourcePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourcePointer.setStatus("current")


class _MplsTunnelInstancePriority_Type(Integer32):
    """Custom type mplsTunnelInstancePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelInstancePriority_Type.__name__ = "Integer32"
_MplsTunnelInstancePriority_Object = MibTableColumn
mplsTunnelInstancePriority = _MplsTunnelInstancePriority_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 16),
    _MplsTunnelInstancePriority_Type()
)
mplsTunnelInstancePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInstancePriority.setStatus("current")


class _MplsTunnelHopTableIndex_Type(Integer32):
    """Custom type mplsTunnelHopTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelHopTableIndex_Type.__name__ = "Integer32"
_MplsTunnelHopTableIndex_Object = MibTableColumn
mplsTunnelHopTableIndex = _MplsTunnelHopTableIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 17),
    _MplsTunnelHopTableIndex_Type()
)
mplsTunnelHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopTableIndex.setStatus("current")


class _MplsTunnelARHopTableIndex_Type(Integer32):
    """Custom type mplsTunnelARHopTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelARHopTableIndex_Type.__name__ = "Integer32"
_MplsTunnelARHopTableIndex_Object = MibTableColumn
mplsTunnelARHopTableIndex = _MplsTunnelARHopTableIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 18),
    _MplsTunnelARHopTableIndex_Type()
)
mplsTunnelARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopTableIndex.setStatus("current")


class _MplsTunnelAdminStatus_Type(Integer32):
    """Custom type mplsTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_MplsTunnelAdminStatus_Type.__name__ = "Integer32"
_MplsTunnelAdminStatus_Object = MibTableColumn
mplsTunnelAdminStatus = _MplsTunnelAdminStatus_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 19),
    _MplsTunnelAdminStatus_Type()
)
mplsTunnelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAdminStatus.setStatus("current")


class _MplsTunnelOperStatus_Type(Integer32):
    """Custom type mplsTunnelOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_MplsTunnelOperStatus_Type.__name__ = "Integer32"
_MplsTunnelOperStatus_Object = MibTableColumn
mplsTunnelOperStatus = _MplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 20),
    _MplsTunnelOperStatus_Type()
)
mplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOperStatus.setStatus("current")
_MplsTunnelRowStatus_Type = RowStatus
_MplsTunnelRowStatus_Object = MibTableColumn
mplsTunnelRowStatus = _MplsTunnelRowStatus_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 21),
    _MplsTunnelRowStatus_Type()
)
mplsTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRowStatus.setStatus("current")
_MplsTunnelStorageType_Type = StorageType
_MplsTunnelStorageType_Object = MibTableColumn
mplsTunnelStorageType = _MplsTunnelStorageType_Object(
    (1, 3, 6, 1, 3, 95, 1, 2, 1, 22),
    _MplsTunnelStorageType_Type()
)
mplsTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelStorageType.setStatus("current")


class _MplsTunnelMaxHops_Type(Integer32):
    """Custom type mplsTunnelMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelMaxHops_Type.__name__ = "Integer32"
_MplsTunnelMaxHops_Object = MibScalar
mplsTunnelMaxHops = _MplsTunnelMaxHops_Object(
    (1, 3, 6, 1, 3, 95, 1, 3),
    _MplsTunnelMaxHops_Type()
)
mplsTunnelMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelMaxHops.setStatus("current")


class _MplsTunnelHopIndexNext_Type(Integer32):
    """Custom type mplsTunnelHopIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelHopIndexNext_Type.__name__ = "Integer32"
_MplsTunnelHopIndexNext_Object = MibScalar
mplsTunnelHopIndexNext = _MplsTunnelHopIndexNext_Object(
    (1, 3, 6, 1, 3, 95, 1, 4),
    _MplsTunnelHopIndexNext_Type()
)
mplsTunnelHopIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelHopIndexNext.setStatus("current")
_MplsTunnelHopTable_Object = MibTable
mplsTunnelHopTable = _MplsTunnelHopTable_Object(
    (1, 3, 6, 1, 3, 95, 1, 5)
)
if mibBuilder.loadTexts:
    mplsTunnelHopTable.setStatus("current")
_MplsTunnelHopEntry_Object = MibTableRow
mplsTunnelHopEntry = _MplsTunnelHopEntry_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1)
)
mplsTunnelHopEntry.setIndexNames(
    (0, "MPLS-TE-MIB", "mplsTunnelHopListIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelHopEntry.setStatus("current")


class _MplsTunnelHopListIndex_Type(Integer32):
    """Custom type mplsTunnelHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelHopListIndex_Type.__name__ = "Integer32"
_MplsTunnelHopListIndex_Object = MibTableColumn
mplsTunnelHopListIndex = _MplsTunnelHopListIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 1),
    _MplsTunnelHopListIndex_Type()
)
mplsTunnelHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndex.setStatus("current")


class _MplsTunnelHopIndex_Type(Integer32):
    """Custom type mplsTunnelHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelHopIndex_Type.__name__ = "Integer32"
_MplsTunnelHopIndex_Object = MibTableColumn
mplsTunnelHopIndex = _MplsTunnelHopIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 2),
    _MplsTunnelHopIndex_Type()
)
mplsTunnelHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopIndex.setStatus("current")


class _MplsTunnelHopAddrType_Type(Integer32):
    """Custom type mplsTunnelHopAddrType based on Integer32"""
    defaultValue = 1

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
        *(("ipV4", 1),
          ("ipV6", 2),
          ("asNumber", 3),
          ("lspid", 4))
    )


_MplsTunnelHopAddrType_Type.__name__ = "Integer32"
_MplsTunnelHopAddrType_Object = MibTableColumn
mplsTunnelHopAddrType = _MplsTunnelHopAddrType_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 3),
    _MplsTunnelHopAddrType_Type()
)
mplsTunnelHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrType.setStatus("current")
_MplsTunnelHopIpv4Addr_Type = IpAddress
_MplsTunnelHopIpv4Addr_Object = MibTableColumn
mplsTunnelHopIpv4Addr = _MplsTunnelHopIpv4Addr_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 4),
    _MplsTunnelHopIpv4Addr_Type()
)
mplsTunnelHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv4Addr.setStatus("current")


class _MplsTunnelHopIpv4PrefixLen_Type(Integer32):
    """Custom type mplsTunnelHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MplsTunnelHopIpv4PrefixLen_Type.__name__ = "Integer32"
_MplsTunnelHopIpv4PrefixLen_Object = MibTableColumn
mplsTunnelHopIpv4PrefixLen = _MplsTunnelHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 5),
    _MplsTunnelHopIpv4PrefixLen_Type()
)
mplsTunnelHopIpv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv4PrefixLen.setStatus("current")
_MplsTunnelHopIpv6Addr_Type = InetAddressIPv6
_MplsTunnelHopIpv6Addr_Object = MibTableColumn
mplsTunnelHopIpv6Addr = _MplsTunnelHopIpv6Addr_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 6),
    _MplsTunnelHopIpv6Addr_Type()
)
mplsTunnelHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv6Addr.setStatus("current")


class _MplsTunnelHopIpv6PrefixLen_Type(Integer32):
    """Custom type mplsTunnelHopIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MplsTunnelHopIpv6PrefixLen_Type.__name__ = "Integer32"
_MplsTunnelHopIpv6PrefixLen_Object = MibTableColumn
mplsTunnelHopIpv6PrefixLen = _MplsTunnelHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 7),
    _MplsTunnelHopIpv6PrefixLen_Type()
)
mplsTunnelHopIpv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv6PrefixLen.setStatus("current")


class _MplsTunnelHopAsNumber_Type(Integer32):
    """Custom type mplsTunnelHopAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelHopAsNumber_Type.__name__ = "Integer32"
_MplsTunnelHopAsNumber_Object = MibTableColumn
mplsTunnelHopAsNumber = _MplsTunnelHopAsNumber_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 8),
    _MplsTunnelHopAsNumber_Type()
)
mplsTunnelHopAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAsNumber.setStatus("current")
_MplsTunnelHopLspId_Type = MplsLSPID
_MplsTunnelHopLspId_Object = MibTableColumn
mplsTunnelHopLspId = _MplsTunnelHopLspId_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 9),
    _MplsTunnelHopLspId_Type()
)
mplsTunnelHopLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopLspId.setStatus("current")


class _MplsTunnelHopStrictOrLoose_Type(Integer32):
    """Custom type mplsTunnelHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_MplsTunnelHopStrictOrLoose_Type.__name__ = "Integer32"
_MplsTunnelHopStrictOrLoose_Object = MibTableColumn
mplsTunnelHopStrictOrLoose = _MplsTunnelHopStrictOrLoose_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 10),
    _MplsTunnelHopStrictOrLoose_Type()
)
mplsTunnelHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopStrictOrLoose.setStatus("current")
_MplsTunnelHopRowStatus_Type = RowStatus
_MplsTunnelHopRowStatus_Object = MibTableColumn
mplsTunnelHopRowStatus = _MplsTunnelHopRowStatus_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 11),
    _MplsTunnelHopRowStatus_Type()
)
mplsTunnelHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopRowStatus.setStatus("current")
_MplsTunnelHopStorageType_Type = StorageType
_MplsTunnelHopStorageType_Object = MibTableColumn
mplsTunnelHopStorageType = _MplsTunnelHopStorageType_Object(
    (1, 3, 6, 1, 3, 95, 1, 5, 1, 12),
    _MplsTunnelHopStorageType_Type()
)
mplsTunnelHopStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopStorageType.setStatus("current")


class _MplsTunnelResourceIndexNext_Type(Integer32):
    """Custom type mplsTunnelResourceIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelResourceIndexNext_Type.__name__ = "Integer32"
_MplsTunnelResourceIndexNext_Object = MibScalar
mplsTunnelResourceIndexNext = _MplsTunnelResourceIndexNext_Object(
    (1, 3, 6, 1, 3, 95, 1, 6),
    _MplsTunnelResourceIndexNext_Type()
)
mplsTunnelResourceIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNext.setStatus("current")
_MplsTunnelResourceTable_Object = MibTable
mplsTunnelResourceTable = _MplsTunnelResourceTable_Object(
    (1, 3, 6, 1, 3, 95, 1, 7)
)
if mibBuilder.loadTexts:
    mplsTunnelResourceTable.setStatus("current")
_MplsTunnelResourceEntry_Object = MibTableRow
mplsTunnelResourceEntry = _MplsTunnelResourceEntry_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1)
)
mplsTunnelResourceEntry.setIndexNames(
    (0, "MPLS-TE-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelResourceEntry.setStatus("current")


class _MplsTunnelResourceIndex_Type(Integer32):
    """Custom type mplsTunnelResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelResourceIndex_Type.__name__ = "Integer32"
_MplsTunnelResourceIndex_Object = MibTableColumn
mplsTunnelResourceIndex = _MplsTunnelResourceIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 1),
    _MplsTunnelResourceIndex_Type()
)
mplsTunnelResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndex.setStatus("current")
_MplsTunnelResourceMaxRate_Type = MplsBitRate
_MplsTunnelResourceMaxRate_Object = MibTableColumn
mplsTunnelResourceMaxRate = _MplsTunnelResourceMaxRate_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 2),
    _MplsTunnelResourceMaxRate_Type()
)
mplsTunnelResourceMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setUnits("bits per second")
_MplsTunnelResourceMeanRate_Type = MplsBitRate
_MplsTunnelResourceMeanRate_Object = MibTableColumn
mplsTunnelResourceMeanRate = _MplsTunnelResourceMeanRate_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 3),
    _MplsTunnelResourceMeanRate_Type()
)
mplsTunnelResourceMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setUnits("bits per second")
_MplsTunnelResourceMaxBurstSize_Type = MplsBurstSize
_MplsTunnelResourceMaxBurstSize_Object = MibTableColumn
mplsTunnelResourceMaxBurstSize = _MplsTunnelResourceMaxBurstSize_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 4),
    _MplsTunnelResourceMaxBurstSize_Type()
)
mplsTunnelResourceMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setUnits("bytes")
_MplsTunnelResourceRowStatus_Type = RowStatus
_MplsTunnelResourceRowStatus_Object = MibTableColumn
mplsTunnelResourceRowStatus = _MplsTunnelResourceRowStatus_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 5),
    _MplsTunnelResourceRowStatus_Type()
)
mplsTunnelResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceRowStatus.setStatus("current")
_MplsTunnelResourceStorageType_Type = StorageType
_MplsTunnelResourceStorageType_Object = MibTableColumn
mplsTunnelResourceStorageType = _MplsTunnelResourceStorageType_Object(
    (1, 3, 6, 1, 3, 95, 1, 7, 1, 6),
    _MplsTunnelResourceStorageType_Type()
)
mplsTunnelResourceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceStorageType.setStatus("current")
_MplsTunnelARHopTable_Object = MibTable
mplsTunnelARHopTable = _MplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 3, 95, 1, 8)
)
if mibBuilder.loadTexts:
    mplsTunnelARHopTable.setStatus("current")
_MplsTunnelARHopEntry_Object = MibTableRow
mplsTunnelARHopEntry = _MplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1)
)
mplsTunnelARHopEntry.setIndexNames(
    (0, "MPLS-TE-MIB", "mplsTunnelARHopListIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelARHopEntry.setStatus("current")


class _MplsTunnelARHopListIndex_Type(Integer32):
    """Custom type mplsTunnelARHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelARHopListIndex_Type.__name__ = "Integer32"
_MplsTunnelARHopListIndex_Object = MibTableColumn
mplsTunnelARHopListIndex = _MplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 1),
    _MplsTunnelARHopListIndex_Type()
)
mplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopListIndex.setStatus("current")


class _MplsTunnelARHopIndex_Type(Integer32):
    """Custom type mplsTunnelARHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelARHopIndex_Type.__name__ = "Integer32"
_MplsTunnelARHopIndex_Object = MibTableColumn
mplsTunnelARHopIndex = _MplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 2),
    _MplsTunnelARHopIndex_Type()
)
mplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopIndex.setStatus("current")


class _MplsTunnelARHopAddrType_Type(Integer32):
    """Custom type mplsTunnelARHopAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipV4", 1),
          ("ipV6", 2),
          ("asNumber", 3))
    )


_MplsTunnelARHopAddrType_Type.__name__ = "Integer32"
_MplsTunnelARHopAddrType_Object = MibTableColumn
mplsTunnelARHopAddrType = _MplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 3),
    _MplsTunnelARHopAddrType_Type()
)
mplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrType.setStatus("current")
_MplsTunnelARHopIpv4Addr_Type = IpAddress
_MplsTunnelARHopIpv4Addr_Object = MibTableColumn
mplsTunnelARHopIpv4Addr = _MplsTunnelARHopIpv4Addr_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 4),
    _MplsTunnelARHopIpv4Addr_Type()
)
mplsTunnelARHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv4Addr.setStatus("current")


class _MplsTunnelARHopIpv4PrefixLen_Type(Integer32):
    """Custom type mplsTunnelARHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MplsTunnelARHopIpv4PrefixLen_Type.__name__ = "Integer32"
_MplsTunnelARHopIpv4PrefixLen_Object = MibTableColumn
mplsTunnelARHopIpv4PrefixLen = _MplsTunnelARHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 5),
    _MplsTunnelARHopIpv4PrefixLen_Type()
)
mplsTunnelARHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv4PrefixLen.setStatus("current")
_MplsTunnelARHopIpv6Addr_Type = InetAddressIPv6
_MplsTunnelARHopIpv6Addr_Object = MibTableColumn
mplsTunnelARHopIpv6Addr = _MplsTunnelARHopIpv6Addr_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 6),
    _MplsTunnelARHopIpv6Addr_Type()
)
mplsTunnelARHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv6Addr.setStatus("current")


class _MplsTunnelARHopIpv6PrefixLen_Type(Integer32):
    """Custom type mplsTunnelARHopIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MplsTunnelARHopIpv6PrefixLen_Type.__name__ = "Integer32"
_MplsTunnelARHopIpv6PrefixLen_Object = MibTableColumn
mplsTunnelARHopIpv6PrefixLen = _MplsTunnelARHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 7),
    _MplsTunnelARHopIpv6PrefixLen_Type()
)
mplsTunnelARHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv6PrefixLen.setStatus("current")


class _MplsTunnelARHopAsNumber_Type(Integer32):
    """Custom type mplsTunnelARHopAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelARHopAsNumber_Type.__name__ = "Integer32"
_MplsTunnelARHopAsNumber_Object = MibTableColumn
mplsTunnelARHopAsNumber = _MplsTunnelARHopAsNumber_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 8),
    _MplsTunnelARHopAsNumber_Type()
)
mplsTunnelARHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAsNumber.setStatus("current")


class _MplsTunnelARHopStrictOrLoose_Type(Integer32):
    """Custom type mplsTunnelARHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_MplsTunnelARHopStrictOrLoose_Type.__name__ = "Integer32"
_MplsTunnelARHopStrictOrLoose_Object = MibTableColumn
mplsTunnelARHopStrictOrLoose = _MplsTunnelARHopStrictOrLoose_Object(
    (1, 3, 6, 1, 3, 95, 1, 8, 1, 9),
    _MplsTunnelARHopStrictOrLoose_Type()
)
mplsTunnelARHopStrictOrLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopStrictOrLoose.setStatus("current")


class _MplsTunnelTrapEnable_Type(TruthValue):
    """Custom type mplsTunnelTrapEnable based on TruthValue"""
    defaultValue = 2


_MplsTunnelTrapEnable_Type.__name__ = "TruthValue"
_MplsTunnelTrapEnable_Object = MibScalar
mplsTunnelTrapEnable = _MplsTunnelTrapEnable_Object(
    (1, 3, 6, 1, 3, 95, 1, 9),
    _MplsTunnelTrapEnable_Type()
)
mplsTunnelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelTrapEnable.setStatus("current")
_MplsTeNotifications_ObjectIdentity = ObjectIdentity
mplsTeNotifications = _MplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 2)
)
_MplsTeNotifyPrefix_ObjectIdentity = ObjectIdentity
mplsTeNotifyPrefix = _MplsTeNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 2, 0)
)
_MplsTeConformance_ObjectIdentity = ObjectIdentity
mplsTeConformance = _MplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 3)
)
_MplsTeGroups_ObjectIdentity = ObjectIdentity
mplsTeGroups = _MplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 3, 1)
)
_MplsTeCompliances_ObjectIdentity = ObjectIdentity
mplsTeCompliances = _MplsTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 95, 3, 2)
)

# Managed Objects groups

mplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 1)
)
mplsTunnelGroup.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelIndexNext"),
        ("MPLS-TE-MIB", "mplsTunnelName"),
        ("MPLS-TE-MIB", "mplsTunnelDescr"),
        ("MPLS-TE-MIB", "mplsTunnelOwner"),
        ("MPLS-TE-MIB", "mplsTunnelXCPointer"),
        ("MPLS-TE-MIB", "mplsTunnelIfIndex"),
        ("MPLS-TE-MIB", "mplsTunnelHopTableIndex"),
        ("MPLS-TE-MIB", "mplsTunnelARHopTableIndex"),
        ("MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-MIB", "mplsTunnelRowStatus"),
        ("MPLS-TE-MIB", "mplsTunnelTrapEnable"),
        ("MPLS-TE-MIB", "mplsTunnelStorageType"),
        ("MPLS-TE-MIB", "mplsTunnelMaxHops"),
        ("MPLS-TE-MIB", "mplsTunnelResourcePointer"),
        ("MPLS-TE-MIB", "mplsTunnelInstancePriority"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroup.setStatus("current")

mplsTunnelManualGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 2)
)
mplsTunnelManualGroup.setObjects(
    ("MPLS-TE-MIB", "mplsTunnelSignallingProto")
)
if mibBuilder.loadTexts:
    mplsTunnelManualGroup.setStatus("current")

mplsTunnelSignaledGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 3)
)
mplsTunnelSignaledGroup.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelSetupPrio"),
        ("MPLS-TE-MIB", "mplsTunnelHoldingPrio"),
        ("MPLS-TE-MIB", "mplsTunnelSignallingProto"),
        ("MPLS-TE-MIB", "mplsTunnelLocalProtectInUse"),
        ("MPLS-TE-MIB", "mplsTunnelSessionAttributes"),
        ("MPLS-TE-MIB", "mplsTunnelHopIndexNext"),
        ("MPLS-TE-MIB", "mplsTunnelHopAddrType"),
        ("MPLS-TE-MIB", "mplsTunnelHopIpv4Addr"),
        ("MPLS-TE-MIB", "mplsTunnelHopIpv4PrefixLen"),
        ("MPLS-TE-MIB", "mplsTunnelHopIpv6Addr"),
        ("MPLS-TE-MIB", "mplsTunnelHopIpv6PrefixLen"),
        ("MPLS-TE-MIB", "mplsTunnelHopAsNumber"),
        ("MPLS-TE-MIB", "mplsTunnelHopLspId"),
        ("MPLS-TE-MIB", "mplsTunnelHopStrictOrLoose"),
        ("MPLS-TE-MIB", "mplsTunnelHopRowStatus"),
        ("MPLS-TE-MIB", "mplsTunnelHopStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelSignaledGroup.setStatus("current")

mplsTunnelIsIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 4)
)
mplsTunnelIsIntfcGroup.setObjects(
    ("MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsIntfcGroup.setStatus("current")

mplsTunnelIsNotIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 5)
)
mplsTunnelIsNotIntfcGroup.setObjects(
    ("MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsNotIntfcGroup.setStatus("current")

mplsTunnelOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 6)
)
mplsTunnelOptionalGroup.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelResourceIndexNext"),
        ("MPLS-TE-MIB", "mplsTunnelResourceMaxRate"),
        ("MPLS-TE-MIB", "mplsTunnelResourceMeanRate"),
        ("MPLS-TE-MIB", "mplsTunnelResourceMaxBurstSize"),
        ("MPLS-TE-MIB", "mplsTunnelResourceRowStatus"),
        ("MPLS-TE-MIB", "mplsTunnelResourceStorageType"),
        ("MPLS-TE-MIB", "mplsTunnelARHopAddrType"),
        ("MPLS-TE-MIB", "mplsTunnelARHopIpv4Addr"),
        ("MPLS-TE-MIB", "mplsTunnelARHopIpv4PrefixLen"),
        ("MPLS-TE-MIB", "mplsTunnelARHopIpv6Addr"),
        ("MPLS-TE-MIB", "mplsTunnelARHopIpv6PrefixLen"),
        ("MPLS-TE-MIB", "mplsTunnelARHopAsNumber"),
        ("MPLS-TE-MIB", "mplsTunnelARHopStrictOrLoose"))
)
if mibBuilder.loadTexts:
    mplsTunnelOptionalGroup.setStatus("current")


# Notification objects

mplsTunnelUp = NotificationType(
    (1, 3, 6, 1, 3, 95, 2, 0, 1)
)
mplsTunnelUp.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelUp.setStatus(
        "current"
    )

mplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 3, 95, 2, 0, 2)
)
mplsTunnelDown.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelDown.setStatus(
        "current"
    )

mplsTunnelRerouted = NotificationType(
    (1, 3, 6, 1, 3, 95, 2, 0, 3)
)
mplsTunnelRerouted.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelRerouted.setStatus(
        "current"
    )

mplsTunnelReoptimized = NotificationType(
    (1, 3, 6, 1, 3, 95, 2, 0, 4)
)
mplsTunnelReoptimized.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelReoptimized.setStatus(
        "current"
    )


# Notifications groups

mplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 95, 3, 1, 7)
)
mplsTeNotificationGroup.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelUp"),
        ("MPLS-TE-MIB", "mplsTunnelDown"),
        ("MPLS-TE-MIB", "mplsTunnelRerouted"))
)
if mibBuilder.loadTexts:
    mplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsTeModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 95, 3, 2, 1)
)
mplsTeModuleCompliance.setObjects(
      *(("MPLS-TE-MIB", "mplsTunnelGroup"),
        ("MPLS-TE-MIB", "mplsTunnelManualGroup"),
        ("MPLS-TE-MIB", "mplsTunnelSignaledGroup"),
        ("MPLS-TE-MIB", "mplsTunnelIsNotIntfcGroup"),
        ("MPLS-TE-MIB", "mplsTunnelIsIntfcGroup"),
        ("MPLS-TE-MIB", "mplsTunnelOptionalGroup"))
)
if mibBuilder.loadTexts:
    mplsTeModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-TE-MIB",
    **{"MplsLSPID": MplsLSPID,
       "MplsBitRate": MplsBitRate,
       "MplsBurstSize": MplsBurstSize,
       "MplsTunnelIndex": MplsTunnelIndex,
       "mplsTeMIB": mplsTeMIB,
       "mplsTeObjects": mplsTeObjects,
       "mplsTunnelIndexNext": mplsTunnelIndexNext,
       "mplsTunnelTable": mplsTunnelTable,
       "mplsTunnelEntry": mplsTunnelEntry,
       "mplsTunnelIndex": mplsTunnelIndex,
       "mplsTunnelInstance": mplsTunnelInstance,
       "mplsTunnelIngressLSRId": mplsTunnelIngressLSRId,
       "mplsTunnelName": mplsTunnelName,
       "mplsTunnelDescr": mplsTunnelDescr,
       "mplsTunnelIsIf": mplsTunnelIsIf,
       "mplsTunnelIfIndex": mplsTunnelIfIndex,
       "mplsTunnelXCPointer": mplsTunnelXCPointer,
       "mplsTunnelSignallingProto": mplsTunnelSignallingProto,
       "mplsTunnelSetupPrio": mplsTunnelSetupPrio,
       "mplsTunnelHoldingPrio": mplsTunnelHoldingPrio,
       "mplsTunnelSessionAttributes": mplsTunnelSessionAttributes,
       "mplsTunnelOwner": mplsTunnelOwner,
       "mplsTunnelLocalProtectInUse": mplsTunnelLocalProtectInUse,
       "mplsTunnelResourcePointer": mplsTunnelResourcePointer,
       "mplsTunnelInstancePriority": mplsTunnelInstancePriority,
       "mplsTunnelHopTableIndex": mplsTunnelHopTableIndex,
       "mplsTunnelARHopTableIndex": mplsTunnelARHopTableIndex,
       "mplsTunnelAdminStatus": mplsTunnelAdminStatus,
       "mplsTunnelOperStatus": mplsTunnelOperStatus,
       "mplsTunnelRowStatus": mplsTunnelRowStatus,
       "mplsTunnelStorageType": mplsTunnelStorageType,
       "mplsTunnelMaxHops": mplsTunnelMaxHops,
       "mplsTunnelHopIndexNext": mplsTunnelHopIndexNext,
       "mplsTunnelHopTable": mplsTunnelHopTable,
       "mplsTunnelHopEntry": mplsTunnelHopEntry,
       "mplsTunnelHopListIndex": mplsTunnelHopListIndex,
       "mplsTunnelHopIndex": mplsTunnelHopIndex,
       "mplsTunnelHopAddrType": mplsTunnelHopAddrType,
       "mplsTunnelHopIpv4Addr": mplsTunnelHopIpv4Addr,
       "mplsTunnelHopIpv4PrefixLen": mplsTunnelHopIpv4PrefixLen,
       "mplsTunnelHopIpv6Addr": mplsTunnelHopIpv6Addr,
       "mplsTunnelHopIpv6PrefixLen": mplsTunnelHopIpv6PrefixLen,
       "mplsTunnelHopAsNumber": mplsTunnelHopAsNumber,
       "mplsTunnelHopLspId": mplsTunnelHopLspId,
       "mplsTunnelHopStrictOrLoose": mplsTunnelHopStrictOrLoose,
       "mplsTunnelHopRowStatus": mplsTunnelHopRowStatus,
       "mplsTunnelHopStorageType": mplsTunnelHopStorageType,
       "mplsTunnelResourceIndexNext": mplsTunnelResourceIndexNext,
       "mplsTunnelResourceTable": mplsTunnelResourceTable,
       "mplsTunnelResourceEntry": mplsTunnelResourceEntry,
       "mplsTunnelResourceIndex": mplsTunnelResourceIndex,
       "mplsTunnelResourceMaxRate": mplsTunnelResourceMaxRate,
       "mplsTunnelResourceMeanRate": mplsTunnelResourceMeanRate,
       "mplsTunnelResourceMaxBurstSize": mplsTunnelResourceMaxBurstSize,
       "mplsTunnelResourceRowStatus": mplsTunnelResourceRowStatus,
       "mplsTunnelResourceStorageType": mplsTunnelResourceStorageType,
       "mplsTunnelARHopTable": mplsTunnelARHopTable,
       "mplsTunnelARHopEntry": mplsTunnelARHopEntry,
       "mplsTunnelARHopListIndex": mplsTunnelARHopListIndex,
       "mplsTunnelARHopIndex": mplsTunnelARHopIndex,
       "mplsTunnelARHopAddrType": mplsTunnelARHopAddrType,
       "mplsTunnelARHopIpv4Addr": mplsTunnelARHopIpv4Addr,
       "mplsTunnelARHopIpv4PrefixLen": mplsTunnelARHopIpv4PrefixLen,
       "mplsTunnelARHopIpv6Addr": mplsTunnelARHopIpv6Addr,
       "mplsTunnelARHopIpv6PrefixLen": mplsTunnelARHopIpv6PrefixLen,
       "mplsTunnelARHopAsNumber": mplsTunnelARHopAsNumber,
       "mplsTunnelARHopStrictOrLoose": mplsTunnelARHopStrictOrLoose,
       "mplsTunnelTrapEnable": mplsTunnelTrapEnable,
       "mplsTeNotifications": mplsTeNotifications,
       "mplsTeNotifyPrefix": mplsTeNotifyPrefix,
       "mplsTunnelUp": mplsTunnelUp,
       "mplsTunnelDown": mplsTunnelDown,
       "mplsTunnelRerouted": mplsTunnelRerouted,
       "mplsTunnelReoptimized": mplsTunnelReoptimized,
       "mplsTeConformance": mplsTeConformance,
       "mplsTeGroups": mplsTeGroups,
       "mplsTunnelGroup": mplsTunnelGroup,
       "mplsTunnelManualGroup": mplsTunnelManualGroup,
       "mplsTunnelSignaledGroup": mplsTunnelSignaledGroup,
       "mplsTunnelIsIntfcGroup": mplsTunnelIsIntfcGroup,
       "mplsTunnelIsNotIntfcGroup": mplsTunnelIsNotIntfcGroup,
       "mplsTunnelOptionalGroup": mplsTunnelOptionalGroup,
       "mplsTeNotificationGroup": mplsTeNotificationGroup,
       "mplsTeCompliances": mplsTeCompliances,
       "mplsTeModuleCompliance": mplsTeModuleCompliance}
)
