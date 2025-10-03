# SNMP MIB module (HH3C-VNF-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VNF-DEVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:17 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cVnfDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196)
)
if mibBuilder.loadTexts:
    hh3cVnfDevice.setRevisions(
        ("2021-02-04 00:00",
         "2020-11-18 00:00",
         "2020-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVnfDeviceTable_ObjectIdentity = ObjectIdentity
hh3cVnfDeviceTable = _Hh3cVnfDeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1)
)
_Hh3cVmInfoTable_Object = MibTable
hh3cVmInfoTable = _Hh3cVmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVmInfoTable.setStatus("current")
_Hh3cVmInfoEntry_Object = MibTableRow
hh3cVmInfoEntry = _Hh3cVmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1)
)
hh3cVmInfoEntry.setIndexNames(
    (0, "HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
)
if mibBuilder.loadTexts:
    hh3cVmInfoEntry.setStatus("current")


class _Hh3cVmSlot_Type(Integer32):
    """Custom type hh3cVmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVmSlot_Type.__name__ = "Integer32"
_Hh3cVmSlot_Object = MibTableColumn
hh3cVmSlot = _Hh3cVmSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 1),
    _Hh3cVmSlot_Type()
)
hh3cVmSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmSlot.setStatus("current")


class _Hh3cVmName_Type(DisplayString):
    """Custom type hh3cVmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cVmName_Type.__name__ = "DisplayString"
_Hh3cVmName_Object = MibTableColumn
hh3cVmName = _Hh3cVmName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 2),
    _Hh3cVmName_Type()
)
hh3cVmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmName.setStatus("current")


class _Hh3cVmType_Type(Integer32):
    """Custom type hh3cVmType based on Integer32"""
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
        *(("other", 1),
          ("ctrlvm", 2),
          ("brasvm", 3),
          ("fwdvm", 4))
    )


_Hh3cVmType_Type.__name__ = "Integer32"
_Hh3cVmType_Object = MibTableColumn
hh3cVmType = _Hh3cVmType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 3),
    _Hh3cVmType_Type()
)
hh3cVmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmType.setStatus("current")


class _Hh3cVmState_Type(Integer32):
    """Custom type hh3cVmState based on Integer32"""
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
        *(("absent", 1),
          ("normal", 2),
          ("fault", 3),
          ("other", 4))
    )


_Hh3cVmState_Type.__name__ = "Integer32"
_Hh3cVmState_Object = MibTableColumn
hh3cVmState = _Hh3cVmState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 4),
    _Hh3cVmState_Type()
)
hh3cVmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmState.setStatus("current")


class _Hh3cVmRole_Type(Integer32):
    """Custom type hh3cVmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("standby", 2),
          ("other", 3))
    )


_Hh3cVmRole_Type.__name__ = "Integer32"
_Hh3cVmRole_Object = MibTableColumn
hh3cVmRole = _Hh3cVmRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 5),
    _Hh3cVmRole_Type()
)
hh3cVmRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmRole.setStatus("current")


class _Hh3cVmRegisterStatus_Type(Integer32):
    """Custom type hh3cVmRegisterStatus based on Integer32"""
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
        *(("registered", 1),
          ("unregistered", 2),
          ("unregisteredDestroying", 3),
          ("registering", 4),
          ("maddown", 5),
          ("unregisteredMaddown", 6),
          ("other", 7))
    )


_Hh3cVmRegisterStatus_Type.__name__ = "Integer32"
_Hh3cVmRegisterStatus_Object = MibTableColumn
hh3cVmRegisterStatus = _Hh3cVmRegisterStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 6),
    _Hh3cVmRegisterStatus_Type()
)
hh3cVmRegisterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmRegisterStatus.setStatus("current")


class _Hh3cVmAttr_Type(Integer32):
    """Custom type hh3cVmAttr based on Integer32"""
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
        *(("initDeploy", 1),
          ("manu", 2),
          ("auto", 3),
          ("autoAccept", 4))
    )


_Hh3cVmAttr_Type.__name__ = "Integer32"
_Hh3cVmAttr_Object = MibTableColumn
hh3cVmAttr = _Hh3cVmAttr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 7),
    _Hh3cVmAttr_Type()
)
hh3cVmAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmAttr.setStatus("current")


class _Hh3cVmGroup_Type(Integer32):
    """Custom type hh3cVmGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVmGroup_Type.__name__ = "Integer32"
_Hh3cVmGroup_Object = MibTableColumn
hh3cVmGroup = _Hh3cVmGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 1, 1, 1, 8),
    _Hh3cVmGroup_Type()
)
hh3cVmGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVmGroup.setStatus("current")
_Hh3cVnfDeviceTraps_ObjectIdentity = ObjectIdentity
hh3cVnfDeviceTraps = _Hh3cVnfDeviceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 2)
)
_Hh3cVnfmTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cVnfmTrapPrefix = _Hh3cVnfmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 2, 0)
)
_Hh3cVmInfoTraps_ObjectIdentity = ObjectIdentity
hh3cVmInfoTraps = _Hh3cVmInfoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3)
)
_Hh3cVmInfoTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cVmInfoTrapPrefix = _Hh3cVmInfoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0)
)
_Hh3cVmChannelHealthTraps_ObjectIdentity = ObjectIdentity
hh3cVmChannelHealthTraps = _Hh3cVmChannelHealthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4)
)
_Hh3cVmChannelHealthTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cVmChannelHealthTrapPrefix = _Hh3cVmChannelHealthTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4, 0)
)
_Hh3cVnfTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVnfTrapObjects = _Hh3cVnfTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5)
)
_Hh3cVnfmTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVnfmTrapObjects = _Hh3cVnfmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 1)
)
_Hh3cVnfmIPType_Type = InetAddressType
_Hh3cVnfmIPType_Object = MibScalar
hh3cVnfmIPType = _Hh3cVnfmIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 1, 1),
    _Hh3cVnfmIPType_Type()
)
hh3cVnfmIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVnfmIPType.setStatus("current")
_Hh3cVnfmIP_Type = InetAddress
_Hh3cVnfmIP_Object = MibScalar
hh3cVnfmIP = _Hh3cVnfmIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 1, 2),
    _Hh3cVnfmIP_Type()
)
hh3cVnfmIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVnfmIP.setStatus("current")


class _Hh3cVnfmPort_Type(Unsigned32):
    """Custom type hh3cVnfmPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVnfmPort_Type.__name__ = "Unsigned32"
_Hh3cVnfmPort_Object = MibScalar
hh3cVnfmPort = _Hh3cVnfmPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 1, 3),
    _Hh3cVnfmPort_Type()
)
hh3cVnfmPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVnfmPort.setStatus("current")
_Hh3cVmInfoTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVmInfoTrapObjects = _Hh3cVmInfoTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2)
)


class _Hh3cVmRetryTimes_Type(Unsigned32):
    """Custom type hh3cVmRetryTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVmRetryTimes_Type.__name__ = "Unsigned32"
_Hh3cVmRetryTimes_Object = MibScalar
hh3cVmRetryTimes = _Hh3cVmRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 1),
    _Hh3cVmRetryTimes_Type()
)
hh3cVmRetryTimes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmRetryTimes.setStatus("current")


class _Hh3cVmCreateAttr_Type(Integer32):
    """Custom type hh3cVmCreateAttr based on Integer32"""
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
        *(("initDeploy", 1),
          ("manu", 2),
          ("auto", 3),
          ("autoAccept", 4))
    )


_Hh3cVmCreateAttr_Type.__name__ = "Integer32"
_Hh3cVmCreateAttr_Object = MibScalar
hh3cVmCreateAttr = _Hh3cVmCreateAttr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 2),
    _Hh3cVmCreateAttr_Type()
)
hh3cVmCreateAttr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmCreateAttr.setStatus("current")


class _Hh3cVmCreateFailReason_Type(OctetString):
    """Custom type hh3cVmCreateFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cVmCreateFailReason_Type.__name__ = "OctetString"
_Hh3cVmCreateFailReason_Object = MibScalar
hh3cVmCreateFailReason = _Hh3cVmCreateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 3),
    _Hh3cVmCreateFailReason_Type()
)
hh3cVmCreateFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmCreateFailReason.setStatus("current")


class _Hh3cVmDeleteFailReason_Type(OctetString):
    """Custom type hh3cVmDeleteFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cVmDeleteFailReason_Type.__name__ = "OctetString"
_Hh3cVmDeleteFailReason_Object = MibScalar
hh3cVmDeleteFailReason = _Hh3cVmDeleteFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 4),
    _Hh3cVmDeleteFailReason_Type()
)
hh3cVmDeleteFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmDeleteFailReason.setStatus("current")


class _Hh3cVmInconsistFaultReason_Type(Integer32):
    """Custom type hh3cVmInconsistFaultReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exisitOnLocal", 1),
          ("existOnVnfm", 2))
    )


_Hh3cVmInconsistFaultReason_Type.__name__ = "Integer32"
_Hh3cVmInconsistFaultReason_Object = MibScalar
hh3cVmInconsistFaultReason = _Hh3cVmInconsistFaultReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 5),
    _Hh3cVmInconsistFaultReason_Type()
)
hh3cVmInconsistFaultReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmInconsistFaultReason.setStatus("current")


class _Hh3cVmResetResult_Type(OctetString):
    """Custom type hh3cVmResetResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cVmResetResult_Type.__name__ = "OctetString"
_Hh3cVmResetResult_Object = MibScalar
hh3cVmResetResult = _Hh3cVmResetResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 6),
    _Hh3cVmResetResult_Type()
)
hh3cVmResetResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmResetResult.setStatus("current")


class _Hh3cVmStatusOnVnfm_Type(Integer32):
    """Custom type hh3cVmStatusOnVnfm based on Integer32"""
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
        *(("building", 1),
          ("active", 2),
          ("error", 3),
          ("unknown", 4))
    )


_Hh3cVmStatusOnVnfm_Type.__name__ = "Integer32"
_Hh3cVmStatusOnVnfm_Object = MibScalar
hh3cVmStatusOnVnfm = _Hh3cVmStatusOnVnfm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 2, 7),
    _Hh3cVmStatusOnVnfm_Type()
)
hh3cVmStatusOnVnfm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmStatusOnVnfm.setStatus("current")
_Hh3cVmChannelHealthTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVmChannelHealthTrapObjects = _Hh3cVmChannelHealthTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3)
)


class _Hh3cVmSelfSlot_Type(Unsigned32):
    """Custom type hh3cVmSelfSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVmSelfSlot_Type.__name__ = "Unsigned32"
_Hh3cVmSelfSlot_Object = MibScalar
hh3cVmSelfSlot = _Hh3cVmSelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3, 1),
    _Hh3cVmSelfSlot_Type()
)
hh3cVmSelfSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmSelfSlot.setStatus("current")


class _Hh3cVmPeerSlot_Type(Unsigned32):
    """Custom type hh3cVmPeerSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVmPeerSlot_Type.__name__ = "Unsigned32"
_Hh3cVmPeerSlot_Object = MibScalar
hh3cVmPeerSlot = _Hh3cVmPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3, 2),
    _Hh3cVmPeerSlot_Type()
)
hh3cVmPeerSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmPeerSlot.setStatus("current")


class _Hh3cVmChannelType_Type(Integer32):
    """Custom type hh3cVmChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlchannel", 1),
          ("datachannel", 2))
    )


_Hh3cVmChannelType_Type.__name__ = "Integer32"
_Hh3cVmChannelType_Object = MibScalar
hh3cVmChannelType = _Hh3cVmChannelType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3, 3),
    _Hh3cVmChannelType_Type()
)
hh3cVmChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmChannelType.setStatus("current")


class _Hh3cVmChannelVlan_Type(Unsigned32):
    """Custom type hh3cVmChannelVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cVmChannelVlan_Type.__name__ = "Unsigned32"
_Hh3cVmChannelVlan_Object = MibScalar
hh3cVmChannelVlan = _Hh3cVmChannelVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3, 4),
    _Hh3cVmChannelVlan_Type()
)
hh3cVmChannelVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmChannelVlan.setStatus("current")
_Hh3cVmChannelLinkMacAddress_Type = MacAddress
_Hh3cVmChannelLinkMacAddress_Object = MibScalar
hh3cVmChannelLinkMacAddress = _Hh3cVmChannelLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 5, 3, 5),
    _Hh3cVmChannelLinkMacAddress_Type()
)
hh3cVmChannelLinkMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVmChannelLinkMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cVnfmConnectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 2, 0, 1)
)
hh3cVnfmConnectionFault.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIPType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIP"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmPort"))
)
if mibBuilder.loadTexts:
    hh3cVnfmConnectionFault.setStatus(
        "current"
    )

hh3cVnfmConnectionFaultResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 2, 0, 2)
)
hh3cVnfmConnectionFaultResume.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIPType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIP"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmPort"))
)
if mibBuilder.loadTexts:
    hh3cVnfmConnectionFaultResume.setStatus(
        "current"
    )

hh3cVnvmAuthenFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 2, 0, 3)
)
hh3cVnvmAuthenFault.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIPType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmIP"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVnfmPort"))
)
if mibBuilder.loadTexts:
    hh3cVnvmAuthenFault.setStatus(
        "current"
    )

hh3cVmCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 1)
)
hh3cVmCreate.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"))
)
if mibBuilder.loadTexts:
    hh3cVmCreate.setStatus(
        "current"
    )

hh3cVmDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 2)
)
hh3cVmDelete.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"))
)
if mibBuilder.loadTexts:
    hh3cVmDelete.setStatus(
        "current"
    )

hh3cVmCreateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 3)
)
hh3cVmCreateSuccess.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmRetryTimes"))
)
if mibBuilder.loadTexts:
    hh3cVmCreateSuccess.setStatus(
        "current"
    )

hh3cVmCreateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 4)
)
hh3cVmCreateFail.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmRetryTimes"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmCreateFailReason"))
)
if mibBuilder.loadTexts:
    hh3cVmCreateFail.setStatus(
        "current"
    )

hh3cVmDeleteSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 5)
)
hh3cVmDeleteSuccess.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmRetryTimes"))
)
if mibBuilder.loadTexts:
    hh3cVmDeleteSuccess.setStatus(
        "current"
    )

hh3cVmDeleteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 6)
)
hh3cVmDeleteFail.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmAttr"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmRetryTimes"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmDeleteFailReason"))
)
if mibBuilder.loadTexts:
    hh3cVmDeleteFail.setStatus(
        "current"
    )

hh3cVmInconsist = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 7)
)
hh3cVmInconsist.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmName"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmStatusOnVnfm"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmInconsistFaultReason"))
)
if mibBuilder.loadTexts:
    hh3cVmInconsist.setStatus(
        "current"
    )

hh3cVmInconsistResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 8)
)
hh3cVmInconsistResume.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmName"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmStatusOnVnfm"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmInconsistFaultReason"))
)
if mibBuilder.loadTexts:
    hh3cVmInconsistResume.setStatus(
        "current"
    )

hh3cVmAcceptInconsistVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 9)
)
hh3cVmAcceptInconsistVm.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmName"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"))
)
if mibBuilder.loadTexts:
    hh3cVmAcceptInconsistVm.setStatus(
        "current"
    )

hh3cVmReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 10)
)
hh3cVmReset.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmResetResult"))
)
if mibBuilder.loadTexts:
    hh3cVmReset.setStatus(
        "current"
    )

hh3cVmUnregisterLongtime = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 11)
)
hh3cVmUnregisterLongtime.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmName"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"))
)
if mibBuilder.loadTexts:
    hh3cVmUnregisterLongtime.setStatus(
        "current"
    )

hh3cVmIsolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 3, 0, 12)
)
hh3cVmIsolate.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmGroup"))
)
if mibBuilder.loadTexts:
    hh3cVmIsolate.setStatus(
        "current"
    )

hh3cVmChannelHealthNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4, 0, 1)
)
hh3cVmChannelHealthNormal.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSelfSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmPeerSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelVlan"))
)
if mibBuilder.loadTexts:
    hh3cVmChannelHealthNormal.setStatus(
        "current"
    )

hh3cVmChannelHealthMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4, 0, 2)
)
hh3cVmChannelHealthMinor.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSelfSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmPeerSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelVlan"))
)
if mibBuilder.loadTexts:
    hh3cVmChannelHealthMinor.setStatus(
        "current"
    )

hh3cVmChannelHealthSevere = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4, 0, 3)
)
hh3cVmChannelHealthSevere.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSelfSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmPeerSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelVlan"))
)
if mibBuilder.loadTexts:
    hh3cVmChannelHealthSevere.setStatus(
        "current"
    )

hh3cVmChannelLinkSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 196, 4, 0, 4)
)
hh3cVmChannelLinkSwitch.setObjects(
      *(("HH3C-VNF-DEVICE-MIB", "hh3cVmSelfSlot"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelType"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelVlan"),
        ("HH3C-VNF-DEVICE-MIB", "hh3cVmChannelLinkMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cVmChannelLinkSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VNF-DEVICE-MIB",
    **{"hh3cVnfDevice": hh3cVnfDevice,
       "hh3cVnfDeviceTable": hh3cVnfDeviceTable,
       "hh3cVmInfoTable": hh3cVmInfoTable,
       "hh3cVmInfoEntry": hh3cVmInfoEntry,
       "hh3cVmSlot": hh3cVmSlot,
       "hh3cVmName": hh3cVmName,
       "hh3cVmType": hh3cVmType,
       "hh3cVmState": hh3cVmState,
       "hh3cVmRole": hh3cVmRole,
       "hh3cVmRegisterStatus": hh3cVmRegisterStatus,
       "hh3cVmAttr": hh3cVmAttr,
       "hh3cVmGroup": hh3cVmGroup,
       "hh3cVnfDeviceTraps": hh3cVnfDeviceTraps,
       "hh3cVnfmTrapPrefix": hh3cVnfmTrapPrefix,
       "hh3cVnfmConnectionFault": hh3cVnfmConnectionFault,
       "hh3cVnfmConnectionFaultResume": hh3cVnfmConnectionFaultResume,
       "hh3cVnvmAuthenFault": hh3cVnvmAuthenFault,
       "hh3cVmInfoTraps": hh3cVmInfoTraps,
       "hh3cVmInfoTrapPrefix": hh3cVmInfoTrapPrefix,
       "hh3cVmCreate": hh3cVmCreate,
       "hh3cVmDelete": hh3cVmDelete,
       "hh3cVmCreateSuccess": hh3cVmCreateSuccess,
       "hh3cVmCreateFail": hh3cVmCreateFail,
       "hh3cVmDeleteSuccess": hh3cVmDeleteSuccess,
       "hh3cVmDeleteFail": hh3cVmDeleteFail,
       "hh3cVmInconsist": hh3cVmInconsist,
       "hh3cVmInconsistResume": hh3cVmInconsistResume,
       "hh3cVmAcceptInconsistVm": hh3cVmAcceptInconsistVm,
       "hh3cVmReset": hh3cVmReset,
       "hh3cVmUnregisterLongtime": hh3cVmUnregisterLongtime,
       "hh3cVmIsolate": hh3cVmIsolate,
       "hh3cVmChannelHealthTraps": hh3cVmChannelHealthTraps,
       "hh3cVmChannelHealthTrapPrefix": hh3cVmChannelHealthTrapPrefix,
       "hh3cVmChannelHealthNormal": hh3cVmChannelHealthNormal,
       "hh3cVmChannelHealthMinor": hh3cVmChannelHealthMinor,
       "hh3cVmChannelHealthSevere": hh3cVmChannelHealthSevere,
       "hh3cVmChannelLinkSwitch": hh3cVmChannelLinkSwitch,
       "hh3cVnfTrapObjects": hh3cVnfTrapObjects,
       "hh3cVnfmTrapObjects": hh3cVnfmTrapObjects,
       "hh3cVnfmIPType": hh3cVnfmIPType,
       "hh3cVnfmIP": hh3cVnfmIP,
       "hh3cVnfmPort": hh3cVnfmPort,
       "hh3cVmInfoTrapObjects": hh3cVmInfoTrapObjects,
       "hh3cVmRetryTimes": hh3cVmRetryTimes,
       "hh3cVmCreateAttr": hh3cVmCreateAttr,
       "hh3cVmCreateFailReason": hh3cVmCreateFailReason,
       "hh3cVmDeleteFailReason": hh3cVmDeleteFailReason,
       "hh3cVmInconsistFaultReason": hh3cVmInconsistFaultReason,
       "hh3cVmResetResult": hh3cVmResetResult,
       "hh3cVmStatusOnVnfm": hh3cVmStatusOnVnfm,
       "hh3cVmChannelHealthTrapObjects": hh3cVmChannelHealthTrapObjects,
       "hh3cVmSelfSlot": hh3cVmSelfSlot,
       "hh3cVmPeerSlot": hh3cVmPeerSlot,
       "hh3cVmChannelType": hh3cVmChannelType,
       "hh3cVmChannelVlan": hh3cVmChannelVlan,
       "hh3cVmChannelLinkMacAddress": hh3cVmChannelLinkMacAddress}
)
