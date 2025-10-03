# SNMP MIB module (HH3C-MPLSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-MPLSEXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:17 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
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

hh3cMplsExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142)
)
if mibBuilder.loadTexts:
    hh3cMplsExt.setRevisions(
        ("2018-08-04 18:00",
         "2017-02-17 18:00",
         "2015-06-16 18:00",
         "2014-12-17 12:00",
         "2013-06-13 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMplsExtObjects_ObjectIdentity = ObjectIdentity
hh3cMplsExtObjects = _Hh3cMplsExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1)
)
_Hh3cMplsExtScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMplsExtScalarGroup = _Hh3cMplsExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1)
)


class _Hh3cMplsExtLsrID_Type(OctetString):
    """Custom type hh3cMplsExtLsrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cMplsExtLsrID_Type.__name__ = "OctetString"
_Hh3cMplsExtLsrID_Object = MibScalar
hh3cMplsExtLsrID = _Hh3cMplsExtLsrID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1, 1),
    _Hh3cMplsExtLsrID_Type()
)
hh3cMplsExtLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsExtLsrID.setStatus("current")
_Hh3cMplsExtLdpStatus_Type = TruthValue
_Hh3cMplsExtLdpStatus_Object = MibScalar
hh3cMplsExtLdpStatus = _Hh3cMplsExtLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 1, 2),
    _Hh3cMplsExtLdpStatus_Type()
)
hh3cMplsExtLdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpStatus.setStatus("current")
_Hh3cMplsExtTable_Object = MibTable
hh3cMplsExtTable = _Hh3cMplsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsExtTable.setStatus("current")
_Hh3cMplsExtEntry_Object = MibTableRow
hh3cMplsExtEntry = _Hh3cMplsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1)
)
hh3cMplsExtEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtEntry.setStatus("current")


class _Hh3cMplsExtIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtIndex_Object = MibTableColumn
hh3cMplsExtIndex = _Hh3cMplsExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 1),
    _Hh3cMplsExtIndex_Type()
)
hh3cMplsExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtIndex.setStatus("current")


class _Hh3cMplsExtCapability_Type(TruthValue):
    """Custom type hh3cMplsExtCapability based on TruthValue"""
    defaultValue = 2


_Hh3cMplsExtCapability_Type.__name__ = "TruthValue"
_Hh3cMplsExtCapability_Object = MibTableColumn
hh3cMplsExtCapability = _Hh3cMplsExtCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 2),
    _Hh3cMplsExtCapability_Type()
)
hh3cMplsExtCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtCapability.setStatus("current")


class _Hh3cMplsExtMtu_Type(Unsigned32):
    """Custom type hh3cMplsExtMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 65535),
    )


_Hh3cMplsExtMtu_Type.__name__ = "Unsigned32"
_Hh3cMplsExtMtu_Object = MibTableColumn
hh3cMplsExtMtu = _Hh3cMplsExtMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 3),
    _Hh3cMplsExtMtu_Type()
)
hh3cMplsExtMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtMtu.setStatus("current")
_Hh3cMplsExtRowStatus_Type = RowStatus
_Hh3cMplsExtRowStatus_Object = MibTableColumn
hh3cMplsExtRowStatus = _Hh3cMplsExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 2, 1, 4),
    _Hh3cMplsExtRowStatus_Type()
)
hh3cMplsExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtRowStatus.setStatus("current")
_Hh3cMplsExtLdpTable_Object = MibTable
hh3cMplsExtLdpTable = _Hh3cMplsExtLdpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMplsExtLdpTable.setStatus("current")
_Hh3cMplsExtLdpEntry_Object = MibTableRow
hh3cMplsExtLdpEntry = _Hh3cMplsExtLdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1)
)
hh3cMplsExtLdpEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtLdpIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtLdpEntry.setStatus("current")


class _Hh3cMplsExtLdpIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtLdpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtLdpIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtLdpIndex_Object = MibTableColumn
hh3cMplsExtLdpIndex = _Hh3cMplsExtLdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 1),
    _Hh3cMplsExtLdpIndex_Type()
)
hh3cMplsExtLdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpIndex.setStatus("current")


class _Hh3cMplsExtLdpCapability_Type(TruthValue):
    """Custom type hh3cMplsExtLdpCapability based on TruthValue"""
    defaultValue = 2


_Hh3cMplsExtLdpCapability_Type.__name__ = "TruthValue"
_Hh3cMplsExtLdpCapability_Object = MibTableColumn
hh3cMplsExtLdpCapability = _Hh3cMplsExtLdpCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 2),
    _Hh3cMplsExtLdpCapability_Type()
)
hh3cMplsExtLdpCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpCapability.setStatus("current")
_Hh3cMplsExtLdpRowStatus_Type = RowStatus
_Hh3cMplsExtLdpRowStatus_Object = MibTableColumn
hh3cMplsExtLdpRowStatus = _Hh3cMplsExtLdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 3, 1, 3),
    _Hh3cMplsExtLdpRowStatus_Type()
)
hh3cMplsExtLdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsExtLdpRowStatus.setStatus("current")
_Hh3cMplsExtBfdTable_Object = MibTable
hh3cMplsExtBfdTable = _Hh3cMplsExtBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cMplsExtBfdTable.setStatus("current")
_Hh3cMplsExtBfdEntry_Object = MibTableRow
hh3cMplsExtBfdEntry = _Hh3cMplsExtBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1)
)
hh3cMplsExtBfdEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtBfdLocalDiscr"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtBfdEntry.setStatus("current")


class _Hh3cMplsExtBfdLocalDiscr_Type(Unsigned32):
    """Custom type hh3cMplsExtBfdLocalDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtBfdLocalDiscr_Type.__name__ = "Unsigned32"
_Hh3cMplsExtBfdLocalDiscr_Object = MibTableColumn
hh3cMplsExtBfdLocalDiscr = _Hh3cMplsExtBfdLocalDiscr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 1),
    _Hh3cMplsExtBfdLocalDiscr_Type()
)
hh3cMplsExtBfdLocalDiscr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdLocalDiscr.setStatus("current")


class _Hh3cMplsExtBfdType_Type(Integer32):
    """Custom type hh3cMplsExtBfdType based on Integer32"""
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
        *(("unknown", 1),
          ("lsp", 2),
          ("vpwsPw", 3),
          ("vplsPw", 4),
          ("te", 5))
    )


_Hh3cMplsExtBfdType_Type.__name__ = "Integer32"
_Hh3cMplsExtBfdType_Object = MibTableColumn
hh3cMplsExtBfdType = _Hh3cMplsExtBfdType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 2),
    _Hh3cMplsExtBfdType_Type()
)
hh3cMplsExtBfdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdType.setStatus("current")
_Hh3cMplsExtBfdBindIfIndex_Type = InterfaceIndexOrZero
_Hh3cMplsExtBfdBindIfIndex_Object = MibTableColumn
hh3cMplsExtBfdBindIfIndex = _Hh3cMplsExtBfdBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 3),
    _Hh3cMplsExtBfdBindIfIndex_Type()
)
hh3cMplsExtBfdBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdBindIfIndex.setStatus("current")


class _Hh3cMplsExtBfdBindIfName_Type(DisplayString):
    """Custom type hh3cMplsExtBfdBindIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMplsExtBfdBindIfName_Type.__name__ = "DisplayString"
_Hh3cMplsExtBfdBindIfName_Object = MibTableColumn
hh3cMplsExtBfdBindIfName = _Hh3cMplsExtBfdBindIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 4),
    _Hh3cMplsExtBfdBindIfName_Type()
)
hh3cMplsExtBfdBindIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdBindIfName.setStatus("current")


class _Hh3cMplsExtBfdXcIndex_Type(OctetString):
    """Custom type hh3cMplsExtBfdXcIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cMplsExtBfdXcIndex_Type.__name__ = "OctetString"
_Hh3cMplsExtBfdXcIndex_Object = MibTableColumn
hh3cMplsExtBfdXcIndex = _Hh3cMplsExtBfdXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 5),
    _Hh3cMplsExtBfdXcIndex_Type()
)
hh3cMplsExtBfdXcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdXcIndex.setStatus("current")


class _Hh3cMplsExtBfdPwBackupFlag_Type(Integer32):
    """Custom type hh3cMplsExtBfdPwBackupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("backup", 3))
    )


_Hh3cMplsExtBfdPwBackupFlag_Type.__name__ = "Integer32"
_Hh3cMplsExtBfdPwBackupFlag_Object = MibTableColumn
hh3cMplsExtBfdPwBackupFlag = _Hh3cMplsExtBfdPwBackupFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 6),
    _Hh3cMplsExtBfdPwBackupFlag_Type()
)
hh3cMplsExtBfdPwBackupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwBackupFlag.setStatus("current")


class _Hh3cMplsExtBfdPwId_Type(Unsigned32):
    """Custom type hh3cMplsExtBfdPwId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cMplsExtBfdPwId_Type.__name__ = "Unsigned32"
_Hh3cMplsExtBfdPwId_Object = MibTableColumn
hh3cMplsExtBfdPwId = _Hh3cMplsExtBfdPwId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 7),
    _Hh3cMplsExtBfdPwId_Type()
)
hh3cMplsExtBfdPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwId.setStatus("current")


class _Hh3cMplsExtBfdVsiIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtBfdVsiIndex based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtBfdVsiIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtBfdVsiIndex_Object = MibTableColumn
hh3cMplsExtBfdVsiIndex = _Hh3cMplsExtBfdVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 8),
    _Hh3cMplsExtBfdVsiIndex_Type()
)
hh3cMplsExtBfdVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdVsiIndex.setStatus("current")
_Hh3cMplsExtBfdPwPeerIpType_Type = InetAddressType
_Hh3cMplsExtBfdPwPeerIpType_Object = MibTableColumn
hh3cMplsExtBfdPwPeerIpType = _Hh3cMplsExtBfdPwPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 9),
    _Hh3cMplsExtBfdPwPeerIpType_Type()
)
hh3cMplsExtBfdPwPeerIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwPeerIpType.setStatus("current")
_Hh3cMplsExtBfdPwPeerIp_Type = InetAddress
_Hh3cMplsExtBfdPwPeerIp_Object = MibTableColumn
hh3cMplsExtBfdPwPeerIp = _Hh3cMplsExtBfdPwPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 10),
    _Hh3cMplsExtBfdPwPeerIp_Type()
)
hh3cMplsExtBfdPwPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwPeerIp.setStatus("current")


class _Hh3cMplsExtBfdPwSPE_Type(Integer32):
    """Custom type hh3cMplsExtBfdPwSPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("upe", 2),
          ("spe", 3))
    )


_Hh3cMplsExtBfdPwSPE_Type.__name__ = "Integer32"
_Hh3cMplsExtBfdPwSPE_Object = MibTableColumn
hh3cMplsExtBfdPwSPE = _Hh3cMplsExtBfdPwSPE_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 11),
    _Hh3cMplsExtBfdPwSPE_Type()
)
hh3cMplsExtBfdPwSPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwSPE.setStatus("current")


class _Hh3cMplsExtBfdPwEncapType_Type(Integer32):
    """Custom type hh3cMplsExtBfdPwEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("frDlciMartini", 2),
          ("atmAal5Sdu", 3),
          ("atmTransCell", 4),
          ("vlan", 5),
          ("ethernet", 6),
          ("hdlc", 7),
          ("ppp", 8),
          ("cesom", 9),
          ("atmNto1Vcc", 10),
          ("atmNto1Vpc", 11),
          ("ipInterworking", 12),
          ("atm1to1Vcc", 13),
          ("atm1to1Vpc", 14),
          ("atmAal5Pdu", 15),
          ("frPort", 16),
          ("cep", 17),
          ("satopE1", 18),
          ("satopT1", 19),
          ("satopE3", 20),
          ("satopT3", 21),
          ("esopsnBasic", 22),
          ("tdmoipAal1Mode", 23),
          ("tdmCesopsnWithCas", 24),
          ("tdmoipAal2Mode", 25),
          ("frDlci", 26))
    )


_Hh3cMplsExtBfdPwEncapType_Type.__name__ = "Integer32"
_Hh3cMplsExtBfdPwEncapType_Object = MibTableColumn
hh3cMplsExtBfdPwEncapType = _Hh3cMplsExtBfdPwEncapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 4, 1, 12),
    _Hh3cMplsExtBfdPwEncapType_Type()
)
hh3cMplsExtBfdPwEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtBfdPwEncapType.setStatus("current")
_Hh3cMplsExtVpnStatsTable_Object = MibTable
hh3cMplsExtVpnStatsTable = _Hh3cMplsExtVpnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsTable.setStatus("current")
_Hh3cMplsExtVpnStatsEntry_Object = MibTableRow
hh3cMplsExtVpnStatsEntry = _Hh3cMplsExtVpnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1)
)
hh3cMplsExtVpnStatsEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtVpnStatsVrfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsEntry.setStatus("current")


class _Hh3cMplsExtVpnStatsVrfIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtVpnStatsVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsExtVpnStatsVrfIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtVpnStatsVrfIndex_Object = MibTableColumn
hh3cMplsExtVpnStatsVrfIndex = _Hh3cMplsExtVpnStatsVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 1),
    _Hh3cMplsExtVpnStatsVrfIndex_Type()
)
hh3cMplsExtVpnStatsVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsVrfIndex.setStatus("current")


class _Hh3cMplsExtVpnStatsVpnName_Type(OctetString):
    """Custom type hh3cMplsExtVpnStatsVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cMplsExtVpnStatsVpnName_Type.__name__ = "OctetString"
_Hh3cMplsExtVpnStatsVpnName_Object = MibTableColumn
hh3cMplsExtVpnStatsVpnName = _Hh3cMplsExtVpnStatsVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 2),
    _Hh3cMplsExtVpnStatsVpnName_Type()
)
hh3cMplsExtVpnStatsVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsVpnName.setStatus("current")
_Hh3cMplsExtVpnStatsInOctets_Type = Counter64
_Hh3cMplsExtVpnStatsInOctets_Object = MibTableColumn
hh3cMplsExtVpnStatsInOctets = _Hh3cMplsExtVpnStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 3),
    _Hh3cMplsExtVpnStatsInOctets_Type()
)
hh3cMplsExtVpnStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsInOctets.setStatus("current")
_Hh3cMplsExtVpnStatsInPackets_Type = Counter64
_Hh3cMplsExtVpnStatsInPackets_Object = MibTableColumn
hh3cMplsExtVpnStatsInPackets = _Hh3cMplsExtVpnStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 4),
    _Hh3cMplsExtVpnStatsInPackets_Type()
)
hh3cMplsExtVpnStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsInPackets.setStatus("current")
_Hh3cMplsExtVpnStatsInErrors_Type = Counter64
_Hh3cMplsExtVpnStatsInErrors_Object = MibTableColumn
hh3cMplsExtVpnStatsInErrors = _Hh3cMplsExtVpnStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 5),
    _Hh3cMplsExtVpnStatsInErrors_Type()
)
hh3cMplsExtVpnStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsInErrors.setStatus("current")
_Hh3cMplsExtVpnStatsInDiscards_Type = Counter64
_Hh3cMplsExtVpnStatsInDiscards_Object = MibTableColumn
hh3cMplsExtVpnStatsInDiscards = _Hh3cMplsExtVpnStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 6),
    _Hh3cMplsExtVpnStatsInDiscards_Type()
)
hh3cMplsExtVpnStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsInDiscards.setStatus("current")
_Hh3cMplsExtVpnStatsOutOctets_Type = Counter64
_Hh3cMplsExtVpnStatsOutOctets_Object = MibTableColumn
hh3cMplsExtVpnStatsOutOctets = _Hh3cMplsExtVpnStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 7),
    _Hh3cMplsExtVpnStatsOutOctets_Type()
)
hh3cMplsExtVpnStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsOutOctets.setStatus("current")
_Hh3cMplsExtVpnStatsOutPackets_Type = Counter64
_Hh3cMplsExtVpnStatsOutPackets_Object = MibTableColumn
hh3cMplsExtVpnStatsOutPackets = _Hh3cMplsExtVpnStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 8),
    _Hh3cMplsExtVpnStatsOutPackets_Type()
)
hh3cMplsExtVpnStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsOutPackets.setStatus("current")
_Hh3cMplsExtVpnStatsOutErrors_Type = Counter64
_Hh3cMplsExtVpnStatsOutErrors_Object = MibTableColumn
hh3cMplsExtVpnStatsOutErrors = _Hh3cMplsExtVpnStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 9),
    _Hh3cMplsExtVpnStatsOutErrors_Type()
)
hh3cMplsExtVpnStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsOutErrors.setStatus("current")
_Hh3cMplsExtVpnStatsOutDiscards_Type = Counter64
_Hh3cMplsExtVpnStatsOutDiscards_Object = MibTableColumn
hh3cMplsExtVpnStatsOutDiscards = _Hh3cMplsExtVpnStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 5, 1, 10),
    _Hh3cMplsExtVpnStatsOutDiscards_Type()
)
hh3cMplsExtVpnStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnStatsOutDiscards.setStatus("current")
_Hh3cMplsExtVpnTable_Object = MibTable
hh3cMplsExtVpnTable = _Hh3cMplsExtVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cMplsExtVpnTable.setStatus("current")
_Hh3cMplsExtVpnEntry_Object = MibTableRow
hh3cMplsExtVpnEntry = _Hh3cMplsExtVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 6, 1)
)
hh3cMplsExtVpnEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtVpnName"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtVpnEntry.setStatus("current")


class _Hh3cMplsExtVpnName_Type(OctetString):
    """Custom type hh3cMplsExtVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cMplsExtVpnName_Type.__name__ = "OctetString"
_Hh3cMplsExtVpnName_Object = MibTableColumn
hh3cMplsExtVpnName = _Hh3cMplsExtVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 6, 1, 1),
    _Hh3cMplsExtVpnName_Type()
)
hh3cMplsExtVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtVpnName.setStatus("current")


class _Hh3cMplsExtVrfIndex_Type(Unsigned32):
    """Custom type hh3cMplsExtVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cMplsExtVrfIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsExtVrfIndex_Object = MibTableColumn
hh3cMplsExtVrfIndex = _Hh3cMplsExtVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 6, 1, 2),
    _Hh3cMplsExtVrfIndex_Type()
)
hh3cMplsExtVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtVrfIndex.setStatus("current")
_Hh3cMplsExtStaticLspTable_Object = MibTable
hh3cMplsExtStaticLspTable = _Hh3cMplsExtStaticLspTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspTable.setStatus("current")
_Hh3cMplsExtStaticLspEntry_Object = MibTableRow
hh3cMplsExtStaticLspEntry = _Hh3cMplsExtStaticLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1)
)
hh3cMplsExtStaticLspEntry.setIndexNames(
    (0, "HH3C-MPLSEXT-MIB", "hh3cMplsExtStaticLspName"),
)
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspEntry.setStatus("current")


class _Hh3cMplsExtStaticLspName_Type(OctetString):
    """Custom type hh3cMplsExtStaticLspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cMplsExtStaticLspName_Type.__name__ = "OctetString"
_Hh3cMplsExtStaticLspName_Object = MibTableColumn
hh3cMplsExtStaticLspName = _Hh3cMplsExtStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 1),
    _Hh3cMplsExtStaticLspName_Type()
)
hh3cMplsExtStaticLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspName.setStatus("current")


class _Hh3cMplsExtStaticLspType_Type(Integer32):
    """Custom type hh3cMplsExtStaticLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("transit", 2),
          ("egress", 3))
    )


_Hh3cMplsExtStaticLspType_Type.__name__ = "Integer32"
_Hh3cMplsExtStaticLspType_Object = MibTableColumn
hh3cMplsExtStaticLspType = _Hh3cMplsExtStaticLspType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 2),
    _Hh3cMplsExtStaticLspType_Type()
)
hh3cMplsExtStaticLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspType.setStatus("current")


class _Hh3cMplsExtStaticLspInLabel_Type(Unsigned32):
    """Custom type hh3cMplsExtStaticLspInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_Hh3cMplsExtStaticLspInLabel_Type.__name__ = "Unsigned32"
_Hh3cMplsExtStaticLspInLabel_Object = MibTableColumn
hh3cMplsExtStaticLspInLabel = _Hh3cMplsExtStaticLspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 3),
    _Hh3cMplsExtStaticLspInLabel_Type()
)
hh3cMplsExtStaticLspInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspInLabel.setStatus("current")


class _Hh3cMplsExtStaticLspOutLabel_Type(Unsigned32):
    """Custom type hh3cMplsExtStaticLspOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_Hh3cMplsExtStaticLspOutLabel_Type.__name__ = "Unsigned32"
_Hh3cMplsExtStaticLspOutLabel_Object = MibTableColumn
hh3cMplsExtStaticLspOutLabel = _Hh3cMplsExtStaticLspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 4),
    _Hh3cMplsExtStaticLspOutLabel_Type()
)
hh3cMplsExtStaticLspOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspOutLabel.setStatus("current")
_Hh3cMplsExtStaticLspDestAddr_Type = InetAddressIPv4
_Hh3cMplsExtStaticLspDestAddr_Object = MibTableColumn
hh3cMplsExtStaticLspDestAddr = _Hh3cMplsExtStaticLspDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 5),
    _Hh3cMplsExtStaticLspDestAddr_Type()
)
hh3cMplsExtStaticLspDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspDestAddr.setStatus("current")


class _Hh3cMplsExtStaticLspDestAddrMaskLen_Type(Unsigned32):
    """Custom type hh3cMplsExtStaticLspDestAddrMaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cMplsExtStaticLspDestAddrMaskLen_Type.__name__ = "Unsigned32"
_Hh3cMplsExtStaticLspDestAddrMaskLen_Object = MibTableColumn
hh3cMplsExtStaticLspDestAddrMaskLen = _Hh3cMplsExtStaticLspDestAddrMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 6),
    _Hh3cMplsExtStaticLspDestAddrMaskLen_Type()
)
hh3cMplsExtStaticLspDestAddrMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspDestAddrMaskLen.setStatus("current")
_Hh3cMplsExtStaticLspNextHopAddr_Type = InetAddressIPv4
_Hh3cMplsExtStaticLspNextHopAddr_Object = MibTableColumn
hh3cMplsExtStaticLspNextHopAddr = _Hh3cMplsExtStaticLspNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 7),
    _Hh3cMplsExtStaticLspNextHopAddr_Type()
)
hh3cMplsExtStaticLspNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspNextHopAddr.setStatus("current")
_Hh3cMplsExtStaticLspOutIfIndex_Type = InterfaceIndexOrZero
_Hh3cMplsExtStaticLspOutIfIndex_Object = MibTableColumn
hh3cMplsExtStaticLspOutIfIndex = _Hh3cMplsExtStaticLspOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142, 1, 7, 1, 8),
    _Hh3cMplsExtStaticLspOutIfIndex_Type()
)
hh3cMplsExtStaticLspOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsExtStaticLspOutIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLSEXT-MIB",
    **{"hh3cMplsExt": hh3cMplsExt,
       "hh3cMplsExtObjects": hh3cMplsExtObjects,
       "hh3cMplsExtScalarGroup": hh3cMplsExtScalarGroup,
       "hh3cMplsExtLsrID": hh3cMplsExtLsrID,
       "hh3cMplsExtLdpStatus": hh3cMplsExtLdpStatus,
       "hh3cMplsExtTable": hh3cMplsExtTable,
       "hh3cMplsExtEntry": hh3cMplsExtEntry,
       "hh3cMplsExtIndex": hh3cMplsExtIndex,
       "hh3cMplsExtCapability": hh3cMplsExtCapability,
       "hh3cMplsExtMtu": hh3cMplsExtMtu,
       "hh3cMplsExtRowStatus": hh3cMplsExtRowStatus,
       "hh3cMplsExtLdpTable": hh3cMplsExtLdpTable,
       "hh3cMplsExtLdpEntry": hh3cMplsExtLdpEntry,
       "hh3cMplsExtLdpIndex": hh3cMplsExtLdpIndex,
       "hh3cMplsExtLdpCapability": hh3cMplsExtLdpCapability,
       "hh3cMplsExtLdpRowStatus": hh3cMplsExtLdpRowStatus,
       "hh3cMplsExtBfdTable": hh3cMplsExtBfdTable,
       "hh3cMplsExtBfdEntry": hh3cMplsExtBfdEntry,
       "hh3cMplsExtBfdLocalDiscr": hh3cMplsExtBfdLocalDiscr,
       "hh3cMplsExtBfdType": hh3cMplsExtBfdType,
       "hh3cMplsExtBfdBindIfIndex": hh3cMplsExtBfdBindIfIndex,
       "hh3cMplsExtBfdBindIfName": hh3cMplsExtBfdBindIfName,
       "hh3cMplsExtBfdXcIndex": hh3cMplsExtBfdXcIndex,
       "hh3cMplsExtBfdPwBackupFlag": hh3cMplsExtBfdPwBackupFlag,
       "hh3cMplsExtBfdPwId": hh3cMplsExtBfdPwId,
       "hh3cMplsExtBfdVsiIndex": hh3cMplsExtBfdVsiIndex,
       "hh3cMplsExtBfdPwPeerIpType": hh3cMplsExtBfdPwPeerIpType,
       "hh3cMplsExtBfdPwPeerIp": hh3cMplsExtBfdPwPeerIp,
       "hh3cMplsExtBfdPwSPE": hh3cMplsExtBfdPwSPE,
       "hh3cMplsExtBfdPwEncapType": hh3cMplsExtBfdPwEncapType,
       "hh3cMplsExtVpnStatsTable": hh3cMplsExtVpnStatsTable,
       "hh3cMplsExtVpnStatsEntry": hh3cMplsExtVpnStatsEntry,
       "hh3cMplsExtVpnStatsVrfIndex": hh3cMplsExtVpnStatsVrfIndex,
       "hh3cMplsExtVpnStatsVpnName": hh3cMplsExtVpnStatsVpnName,
       "hh3cMplsExtVpnStatsInOctets": hh3cMplsExtVpnStatsInOctets,
       "hh3cMplsExtVpnStatsInPackets": hh3cMplsExtVpnStatsInPackets,
       "hh3cMplsExtVpnStatsInErrors": hh3cMplsExtVpnStatsInErrors,
       "hh3cMplsExtVpnStatsInDiscards": hh3cMplsExtVpnStatsInDiscards,
       "hh3cMplsExtVpnStatsOutOctets": hh3cMplsExtVpnStatsOutOctets,
       "hh3cMplsExtVpnStatsOutPackets": hh3cMplsExtVpnStatsOutPackets,
       "hh3cMplsExtVpnStatsOutErrors": hh3cMplsExtVpnStatsOutErrors,
       "hh3cMplsExtVpnStatsOutDiscards": hh3cMplsExtVpnStatsOutDiscards,
       "hh3cMplsExtVpnTable": hh3cMplsExtVpnTable,
       "hh3cMplsExtVpnEntry": hh3cMplsExtVpnEntry,
       "hh3cMplsExtVpnName": hh3cMplsExtVpnName,
       "hh3cMplsExtVrfIndex": hh3cMplsExtVrfIndex,
       "hh3cMplsExtStaticLspTable": hh3cMplsExtStaticLspTable,
       "hh3cMplsExtStaticLspEntry": hh3cMplsExtStaticLspEntry,
       "hh3cMplsExtStaticLspName": hh3cMplsExtStaticLspName,
       "hh3cMplsExtStaticLspType": hh3cMplsExtStaticLspType,
       "hh3cMplsExtStaticLspInLabel": hh3cMplsExtStaticLspInLabel,
       "hh3cMplsExtStaticLspOutLabel": hh3cMplsExtStaticLspOutLabel,
       "hh3cMplsExtStaticLspDestAddr": hh3cMplsExtStaticLspDestAddr,
       "hh3cMplsExtStaticLspDestAddrMaskLen": hh3cMplsExtStaticLspDestAddrMaskLen,
       "hh3cMplsExtStaticLspNextHopAddr": hh3cMplsExtStaticLspNextHopAddr,
       "hh3cMplsExtStaticLspOutIfIndex": hh3cMplsExtStaticLspOutIfIndex}
)
