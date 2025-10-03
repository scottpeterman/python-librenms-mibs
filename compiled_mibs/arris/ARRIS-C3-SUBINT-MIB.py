# SNMP MIB module (ARRIS-C3-SUBINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-SUBINT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:09 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmtsC3SubIntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxSubIntObjects_ObjectIdentity = ObjectIdentity
dcxSubIntObjects = _DcxSubIntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1)
)
_DcxSubIntControlGroup_ObjectIdentity = ObjectIdentity
dcxSubIntControlGroup = _DcxSubIntControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1)
)
_DcxSubIntTable_Object = MibTable
dcxSubIntTable = _DcxSubIntTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxSubIntTable.setStatus("current")
_DcxSubIntEntry_Object = MibTableRow
dcxSubIntEntry = _DcxSubIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1)
)
dcxSubIntEntry.setIndexNames(
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"),
)
if mibBuilder.loadTexts:
    dcxSubIntEntry.setStatus("current")


class _DcxSubIntSlotIndex_Type(Unsigned32):
    """Custom type dcxSubIntSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntSlotIndex_Type.__name__ = "Unsigned32"
_DcxSubIntSlotIndex_Object = MibTableColumn
dcxSubIntSlotIndex = _DcxSubIntSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 1),
    _DcxSubIntSlotIndex_Type()
)
dcxSubIntSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntSlotIndex.setStatus("current")


class _DcxSubIntPortIndex_Type(Unsigned32):
    """Custom type dcxSubIntPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntPortIndex_Type.__name__ = "Unsigned32"
_DcxSubIntPortIndex_Object = MibTableColumn
dcxSubIntPortIndex = _DcxSubIntPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 2),
    _DcxSubIntPortIndex_Type()
)
dcxSubIntPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntPortIndex.setStatus("current")


class _DcxSubIntSubIntIndex_Type(Unsigned32):
    """Custom type dcxSubIntSubIntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntSubIntIndex_Type.__name__ = "Unsigned32"
_DcxSubIntSubIntIndex_Object = MibTableColumn
dcxSubIntSubIntIndex = _DcxSubIntSubIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 3),
    _DcxSubIntSubIntIndex_Type()
)
dcxSubIntSubIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntSubIntIndex.setStatus("current")


class _DcxSubIntBridgeGroupNum_Type(Unsigned32):
    """Custom type dcxSubIntBridgeGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_DcxSubIntBridgeGroupNum_Type.__name__ = "Unsigned32"
_DcxSubIntBridgeGroupNum_Object = MibTableColumn
dcxSubIntBridgeGroupNum = _DcxSubIntBridgeGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 4),
    _DcxSubIntBridgeGroupNum_Type()
)
dcxSubIntBridgeGroupNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBridgeGroupNum.setStatus("current")
_DcxSubIntManagementAccess_Type = TruthValue
_DcxSubIntManagementAccess_Object = MibTableColumn
dcxSubIntManagementAccess = _DcxSubIntManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 5),
    _DcxSubIntManagementAccess_Type()
)
dcxSubIntManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntManagementAccess.setStatus("current")
_DcxSubIntPrimaryIpAddress_Type = IpAddress
_DcxSubIntPrimaryIpAddress_Object = MibTableColumn
dcxSubIntPrimaryIpAddress = _DcxSubIntPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 6),
    _DcxSubIntPrimaryIpAddress_Type()
)
dcxSubIntPrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntPrimaryIpAddress.setStatus("current")
_DcxSubIntPrimaryIpMask_Type = IpAddress
_DcxSubIntPrimaryIpMask_Object = MibTableColumn
dcxSubIntPrimaryIpMask = _DcxSubIntPrimaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 7),
    _DcxSubIntPrimaryIpMask_Type()
)
dcxSubIntPrimaryIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntPrimaryIpMask.setStatus("current")
_DcxSubIntPrimaryIpBCastAddress_Type = IpAddress
_DcxSubIntPrimaryIpBCastAddress_Object = MibTableColumn
dcxSubIntPrimaryIpBCastAddress = _DcxSubIntPrimaryIpBCastAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 8),
    _DcxSubIntPrimaryIpBCastAddress_Type()
)
dcxSubIntPrimaryIpBCastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntPrimaryIpBCastAddress.setStatus("current")
_DcxSubIntRelayEnabled_Type = TruthValue
_DcxSubIntRelayEnabled_Object = MibTableColumn
dcxSubIntRelayEnabled = _DcxSubIntRelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 9),
    _DcxSubIntRelayEnabled_Type()
)
dcxSubIntRelayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntRelayEnabled.setStatus("current")
_DcxSubIntRelayInformationOption_Type = TruthValue
_DcxSubIntRelayInformationOption_Object = MibTableColumn
dcxSubIntRelayInformationOption = _DcxSubIntRelayInformationOption_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 10),
    _DcxSubIntRelayInformationOption_Type()
)
dcxSubIntRelayInformationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntRelayInformationOption.setStatus("current")


class _DcxSubIntGiaddrPolicy_Type(Integer32):
    """Custom type dcxSubIntGiaddrPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("primary", 1),
          ("policy", 2))
    )


_DcxSubIntGiaddrPolicy_Type.__name__ = "Integer32"
_DcxSubIntGiaddrPolicy_Object = MibTableColumn
dcxSubIntGiaddrPolicy = _DcxSubIntGiaddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 11),
    _DcxSubIntGiaddrPolicy_Type()
)
dcxSubIntGiaddrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntGiaddrPolicy.setStatus("current")


class _DcxSubIntInboundAclIndex_Type(Unsigned32):
    """Custom type dcxSubIntInboundAclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_DcxSubIntInboundAclIndex_Type.__name__ = "Unsigned32"
_DcxSubIntInboundAclIndex_Object = MibTableColumn
dcxSubIntInboundAclIndex = _DcxSubIntInboundAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 12),
    _DcxSubIntInboundAclIndex_Type()
)
dcxSubIntInboundAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntInboundAclIndex.setStatus("current")


class _DcxSubIntOutgoingAclIndex_Type(Unsigned32):
    """Custom type dcxSubIntOutgoingAclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_DcxSubIntOutgoingAclIndex_Type.__name__ = "Unsigned32"
_DcxSubIntOutgoingAclIndex_Object = MibTableColumn
dcxSubIntOutgoingAclIndex = _DcxSubIntOutgoingAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 13),
    _DcxSubIntOutgoingAclIndex_Type()
)
dcxSubIntOutgoingAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntOutgoingAclIndex.setStatus("current")


class _DcxSubIntUnboundTag_Type(Unsigned32):
    """Custom type dcxSubIntUnboundTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntUnboundTag_Type.__name__ = "Unsigned32"
_DcxSubIntUnboundTag_Object = MibTableColumn
dcxSubIntUnboundTag = _DcxSubIntUnboundTag_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 14),
    _DcxSubIntUnboundTag_Type()
)
dcxSubIntUnboundTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntUnboundTag.setStatus("current")
_DcxSubIntUnboundTagIsNative_Type = TruthValue
_DcxSubIntUnboundTagIsNative_Object = MibTableColumn
dcxSubIntUnboundTagIsNative = _DcxSubIntUnboundTagIsNative_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 15),
    _DcxSubIntUnboundTagIsNative_Type()
)
dcxSubIntUnboundTagIsNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntUnboundTagIsNative.setStatus("current")
_DcxSubIntOperational_Type = TruthValue
_DcxSubIntOperational_Object = MibTableColumn
dcxSubIntOperational = _DcxSubIntOperational_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 16),
    _DcxSubIntOperational_Type()
)
dcxSubIntOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSubIntOperational.setStatus("current")
_DcxSubIntStatus_Type = RowStatus
_DcxSubIntStatus_Object = MibTableColumn
dcxSubIntStatus = _DcxSubIntStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 17),
    _DcxSubIntStatus_Type()
)
dcxSubIntStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxSubIntStatus.setStatus("current")
_DcxSubIntIpTable_Object = MibTable
dcxSubIntIpTable = _DcxSubIntIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dcxSubIntIpTable.setStatus("current")
_DcxSubIntIpEntry_Object = MibTableRow
dcxSubIntIpEntry = _DcxSubIntIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1)
)
dcxSubIntIpEntry.setIndexNames(
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntIpIndex"),
)
if mibBuilder.loadTexts:
    dcxSubIntIpEntry.setStatus("current")
_DcxSubIntIpIndex_Type = Unsigned32
_DcxSubIntIpIndex_Object = MibTableColumn
dcxSubIntIpIndex = _DcxSubIntIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 1),
    _DcxSubIntIpIndex_Type()
)
dcxSubIntIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntIpIndex.setStatus("current")
_DcxSubIntIpAddress_Type = IpAddress
_DcxSubIntIpAddress_Object = MibTableColumn
dcxSubIntIpAddress = _DcxSubIntIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 2),
    _DcxSubIntIpAddress_Type()
)
dcxSubIntIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntIpAddress.setStatus("current")
_DcxSubIntIpMask_Type = IpAddress
_DcxSubIntIpMask_Object = MibTableColumn
dcxSubIntIpMask = _DcxSubIntIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 3),
    _DcxSubIntIpMask_Type()
)
dcxSubIntIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntIpMask.setStatus("current")
_DcxSubIntIpBCastAddress_Type = IpAddress
_DcxSubIntIpBCastAddress_Object = MibTableColumn
dcxSubIntIpBCastAddress = _DcxSubIntIpBCastAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 4),
    _DcxSubIntIpBCastAddress_Type()
)
dcxSubIntIpBCastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntIpBCastAddress.setStatus("current")


class _DcxSubIntIpAddressType_Type(Integer32):
    """Custom type dcxSubIntIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_DcxSubIntIpAddressType_Type.__name__ = "Integer32"
_DcxSubIntIpAddressType_Object = MibTableColumn
dcxSubIntIpAddressType = _DcxSubIntIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 5),
    _DcxSubIntIpAddressType_Type()
)
dcxSubIntIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntIpAddressType.setStatus("current")
_DcxSubIntIpStatus_Type = RowStatus
_DcxSubIntIpStatus_Object = MibTableColumn
dcxSubIntIpStatus = _DcxSubIntIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 6),
    _DcxSubIntIpStatus_Type()
)
dcxSubIntIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxSubIntIpStatus.setStatus("current")
_DcxSubIntCableHelperTable_Object = MibTable
dcxSubIntCableHelperTable = _DcxSubIntCableHelperTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dcxSubIntCableHelperTable.setStatus("current")
_DcxSubIntCableHelperEntry_Object = MibTableRow
dcxSubIntCableHelperEntry = _DcxSubIntCableHelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1)
)
dcxSubIntCableHelperEntry.setIndexNames(
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntCableHelperType"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntCableHelperIndex"),
)
if mibBuilder.loadTexts:
    dcxSubIntCableHelperEntry.setStatus("current")


class _DcxSubIntCableHelperType_Type(Integer32):
    """Custom type dcxSubIntCableHelperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("cm", 1),
          ("cpe", 2))
    )


_DcxSubIntCableHelperType_Type.__name__ = "Integer32"
_DcxSubIntCableHelperType_Object = MibTableColumn
dcxSubIntCableHelperType = _DcxSubIntCableHelperType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 1),
    _DcxSubIntCableHelperType_Type()
)
dcxSubIntCableHelperType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntCableHelperType.setStatus("current")
_DcxSubIntCableHelperIndex_Type = Unsigned32
_DcxSubIntCableHelperIndex_Object = MibTableColumn
dcxSubIntCableHelperIndex = _DcxSubIntCableHelperIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 2),
    _DcxSubIntCableHelperIndex_Type()
)
dcxSubIntCableHelperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntCableHelperIndex.setStatus("current")
_DcxSubIntCableHelperIpAddress_Type = IpAddress
_DcxSubIntCableHelperIpAddress_Object = MibTableColumn
dcxSubIntCableHelperIpAddress = _DcxSubIntCableHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 3),
    _DcxSubIntCableHelperIpAddress_Type()
)
dcxSubIntCableHelperIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntCableHelperIpAddress.setStatus("current")
_DcxSubIntCableHelperStatus_Type = RowStatus
_DcxSubIntCableHelperStatus_Object = MibTableColumn
dcxSubIntCableHelperStatus = _DcxSubIntCableHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 4),
    _DcxSubIntCableHelperStatus_Type()
)
dcxSubIntCableHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxSubIntCableHelperStatus.setStatus("current")
_DcxSubIntVlanTagTable_Object = MibTable
dcxSubIntVlanTagTable = _DcxSubIntVlanTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dcxSubIntVlanTagTable.setStatus("current")
_DcxSubIntVlanTagEntry_Object = MibTableRow
dcxSubIntVlanTagEntry = _DcxSubIntVlanTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1)
)
dcxSubIntVlanTagEntry.setIndexNames(
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"),
    (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntVlanTag"),
)
if mibBuilder.loadTexts:
    dcxSubIntVlanTagEntry.setStatus("current")


class _DcxSubIntVlanTag_Type(Unsigned32):
    """Custom type dcxSubIntVlanTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntVlanTag_Type.__name__ = "Unsigned32"
_DcxSubIntVlanTag_Object = MibTableColumn
dcxSubIntVlanTag = _DcxSubIntVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 1),
    _DcxSubIntVlanTag_Type()
)
dcxSubIntVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSubIntVlanTag.setStatus("current")
_DcxSubIntVlanNative_Type = TruthValue
_DcxSubIntVlanNative_Object = MibTableColumn
dcxSubIntVlanNative = _DcxSubIntVlanNative_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 2),
    _DcxSubIntVlanNative_Type()
)
dcxSubIntVlanNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntVlanNative.setStatus("current")
_DcxSubIntVlanIsBound_Type = TruthValue
_DcxSubIntVlanIsBound_Object = MibTableColumn
dcxSubIntVlanIsBound = _DcxSubIntVlanIsBound_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 3),
    _DcxSubIntVlanIsBound_Type()
)
dcxSubIntVlanIsBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntVlanIsBound.setStatus("current")


class _DcxSubIntBoundVlanSlotIndex_Type(Integer32):
    """Custom type dcxSubIntBoundVlanSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_DcxSubIntBoundVlanSlotIndex_Type.__name__ = "Integer32"
_DcxSubIntBoundVlanSlotIndex_Object = MibTableColumn
dcxSubIntBoundVlanSlotIndex = _DcxSubIntBoundVlanSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 4),
    _DcxSubIntBoundVlanSlotIndex_Type()
)
dcxSubIntBoundVlanSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBoundVlanSlotIndex.setStatus("current")


class _DcxSubIntBoundVlanPortIndex_Type(Integer32):
    """Custom type dcxSubIntBoundVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_DcxSubIntBoundVlanPortIndex_Type.__name__ = "Integer32"
_DcxSubIntBoundVlanPortIndex_Object = MibTableColumn
dcxSubIntBoundVlanPortIndex = _DcxSubIntBoundVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 5),
    _DcxSubIntBoundVlanPortIndex_Type()
)
dcxSubIntBoundVlanPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBoundVlanPortIndex.setStatus("current")


class _DcxSubIntBoundVlanSubIntIndex_Type(Integer32):
    """Custom type dcxSubIntBoundVlanSubIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_DcxSubIntBoundVlanSubIntIndex_Type.__name__ = "Integer32"
_DcxSubIntBoundVlanSubIntIndex_Object = MibTableColumn
dcxSubIntBoundVlanSubIntIndex = _DcxSubIntBoundVlanSubIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 6),
    _DcxSubIntBoundVlanSubIntIndex_Type()
)
dcxSubIntBoundVlanSubIntIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBoundVlanSubIntIndex.setStatus("current")


class _DcxSubIntBoundVlanTag_Type(Unsigned32):
    """Custom type dcxSubIntBoundVlanTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DcxSubIntBoundVlanTag_Type.__name__ = "Unsigned32"
_DcxSubIntBoundVlanTag_Object = MibTableColumn
dcxSubIntBoundVlanTag = _DcxSubIntBoundVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 7),
    _DcxSubIntBoundVlanTag_Type()
)
dcxSubIntBoundVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBoundVlanTag.setStatus("current")
_DcxSubIntBoundVlanNative_Type = TruthValue
_DcxSubIntBoundVlanNative_Object = MibTableColumn
dcxSubIntBoundVlanNative = _DcxSubIntBoundVlanNative_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 8),
    _DcxSubIntBoundVlanNative_Type()
)
dcxSubIntBoundVlanNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSubIntBoundVlanNative.setStatus("current")
_DcxSubIntVlanTagStatus_Type = RowStatus
_DcxSubIntVlanTagStatus_Object = MibTableColumn
dcxSubIntVlanTagStatus = _DcxSubIntVlanTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 9),
    _DcxSubIntVlanTagStatus_Type()
)
dcxSubIntVlanTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxSubIntVlanTagStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-SUBINT-MIB",
    **{"cmtsC3SubIntMIB": cmtsC3SubIntMIB,
       "dcxSubIntObjects": dcxSubIntObjects,
       "dcxSubIntControlGroup": dcxSubIntControlGroup,
       "dcxSubIntTable": dcxSubIntTable,
       "dcxSubIntEntry": dcxSubIntEntry,
       "dcxSubIntSlotIndex": dcxSubIntSlotIndex,
       "dcxSubIntPortIndex": dcxSubIntPortIndex,
       "dcxSubIntSubIntIndex": dcxSubIntSubIntIndex,
       "dcxSubIntBridgeGroupNum": dcxSubIntBridgeGroupNum,
       "dcxSubIntManagementAccess": dcxSubIntManagementAccess,
       "dcxSubIntPrimaryIpAddress": dcxSubIntPrimaryIpAddress,
       "dcxSubIntPrimaryIpMask": dcxSubIntPrimaryIpMask,
       "dcxSubIntPrimaryIpBCastAddress": dcxSubIntPrimaryIpBCastAddress,
       "dcxSubIntRelayEnabled": dcxSubIntRelayEnabled,
       "dcxSubIntRelayInformationOption": dcxSubIntRelayInformationOption,
       "dcxSubIntGiaddrPolicy": dcxSubIntGiaddrPolicy,
       "dcxSubIntInboundAclIndex": dcxSubIntInboundAclIndex,
       "dcxSubIntOutgoingAclIndex": dcxSubIntOutgoingAclIndex,
       "dcxSubIntUnboundTag": dcxSubIntUnboundTag,
       "dcxSubIntUnboundTagIsNative": dcxSubIntUnboundTagIsNative,
       "dcxSubIntOperational": dcxSubIntOperational,
       "dcxSubIntStatus": dcxSubIntStatus,
       "dcxSubIntIpTable": dcxSubIntIpTable,
       "dcxSubIntIpEntry": dcxSubIntIpEntry,
       "dcxSubIntIpIndex": dcxSubIntIpIndex,
       "dcxSubIntIpAddress": dcxSubIntIpAddress,
       "dcxSubIntIpMask": dcxSubIntIpMask,
       "dcxSubIntIpBCastAddress": dcxSubIntIpBCastAddress,
       "dcxSubIntIpAddressType": dcxSubIntIpAddressType,
       "dcxSubIntIpStatus": dcxSubIntIpStatus,
       "dcxSubIntCableHelperTable": dcxSubIntCableHelperTable,
       "dcxSubIntCableHelperEntry": dcxSubIntCableHelperEntry,
       "dcxSubIntCableHelperType": dcxSubIntCableHelperType,
       "dcxSubIntCableHelperIndex": dcxSubIntCableHelperIndex,
       "dcxSubIntCableHelperIpAddress": dcxSubIntCableHelperIpAddress,
       "dcxSubIntCableHelperStatus": dcxSubIntCableHelperStatus,
       "dcxSubIntVlanTagTable": dcxSubIntVlanTagTable,
       "dcxSubIntVlanTagEntry": dcxSubIntVlanTagEntry,
       "dcxSubIntVlanTag": dcxSubIntVlanTag,
       "dcxSubIntVlanNative": dcxSubIntVlanNative,
       "dcxSubIntVlanIsBound": dcxSubIntVlanIsBound,
       "dcxSubIntBoundVlanSlotIndex": dcxSubIntBoundVlanSlotIndex,
       "dcxSubIntBoundVlanPortIndex": dcxSubIntBoundVlanPortIndex,
       "dcxSubIntBoundVlanSubIntIndex": dcxSubIntBoundVlanSubIntIndex,
       "dcxSubIntBoundVlanTag": dcxSubIntBoundVlanTag,
       "dcxSubIntBoundVlanNative": dcxSubIntBoundVlanNative,
       "dcxSubIntVlanTagStatus": dcxSubIntVlanTagStatus}
)
