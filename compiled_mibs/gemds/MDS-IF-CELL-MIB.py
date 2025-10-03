# SNMP MIB module (MDS-IF-CELL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-IF-CELL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mdsInterfaces,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsInterfaces")

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

mdsIfCellMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mdsIfCellMIB.setRevisions(
        ("2019-12-23 00:00",
         "2019-10-11 00:00",
         "2018-05-16 00:00",
         "2018-02-28 00:00",
         "2016-10-11 00:00",
         "2016-02-25 00:00",
         "2015-09-15 00:00",
         "2015-08-03 00:00",
         "2015-07-23 00:00",
         "2015-01-29 00:00",
         "2014-11-25 00:00",
         "2014-10-20 00:00",
         "2013-04-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class SimSlotState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInserted", 0),
          ("inserted", 1))
    )



# MIB Managed Objects in the order of their OIDs

_MIfCellMIBObjects_ObjectIdentity = ObjectIdentity
mIfCellMIBObjects = _MIfCellMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1)
)
_MIfCellConfig_ObjectIdentity = ObjectIdentity
mIfCellConfig = _MIfCellConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 1)
)
_MIfCellStatus_ObjectIdentity = ObjectIdentity
mIfCellStatus = _MIfCellStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2)
)
_MIfCellStatusTable_Object = MibTable
mIfCellStatusTable = _MIfCellStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mIfCellStatusTable.setStatus("current")
_MIfCellStatusEntry_Object = MibTableRow
mIfCellStatusEntry = _MIfCellStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1)
)
mIfCellStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mIfCellStatusEntry.setStatus("current")
_MIfCellImsi_Type = DisplayString
_MIfCellImsi_Object = MibTableColumn
mIfCellImsi = _MIfCellImsi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 1),
    _MIfCellImsi_Type()
)
mIfCellImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellImsi.setStatus("current")
_MIfCellImei_Type = DisplayString
_MIfCellImei_Object = MibTableColumn
mIfCellImei = _MIfCellImei_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 2),
    _MIfCellImei_Type()
)
mIfCellImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellImei.setStatus("current")
_MIfCellIccid_Type = DisplayString
_MIfCellIccid_Object = MibTableColumn
mIfCellIccid = _MIfCellIccid_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 3),
    _MIfCellIccid_Type()
)
mIfCellIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellIccid.setStatus("current")
_MIfCellMdn_Type = DisplayString
_MIfCellMdn_Object = MibTableColumn
mIfCellMdn = _MIfCellMdn_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 4),
    _MIfCellMdn_Type()
)
mIfCellMdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellMdn.setStatus("current")
_MIfCellApn_Type = DisplayString
_MIfCellApn_Object = MibTableColumn
mIfCellApn = _MIfCellApn_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 5),
    _MIfCellApn_Type()
)
mIfCellApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellApn.setStatus("current")
_MIfCellAppSwVersion_Type = DisplayString
_MIfCellAppSwVersion_Object = MibTableColumn
mIfCellAppSwVersion = _MIfCellAppSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 6),
    _MIfCellAppSwVersion_Type()
)
mIfCellAppSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellAppSwVersion.setStatus("current")
_MIfCellModemSwVersion_Type = DisplayString
_MIfCellModemSwVersion_Object = MibTableColumn
mIfCellModemSwVersion = _MIfCellModemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 7),
    _MIfCellModemSwVersion_Type()
)
mIfCellModemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellModemSwVersion.setStatus("current")


class _MIfCellSimState_Type(Integer32):
    """Custom type mIfCellSimState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notInserted", 0),
          ("locked", 1),
          ("ready", 2),
          ("failed", 3),
          ("unknown", 4))
    )


_MIfCellSimState_Type.__name__ = "Integer32"
_MIfCellSimState_Object = MibTableColumn
mIfCellSimState = _MIfCellSimState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 8),
    _MIfCellSimState_Type()
)
mIfCellSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellSimState.setStatus("current")


class _MIfCellModemState_Type(Integer32):
    """Custom type mIfCellModemState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notRegistered", 1),
          ("searching", 2),
          ("registrationDenied", 3),
          ("idle", 4),
          ("connected", 5),
          ("fwRequired", 6))
    )


_MIfCellModemState_Type.__name__ = "Integer32"
_MIfCellModemState_Object = MibTableColumn
mIfCellModemState = _MIfCellModemState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 9),
    _MIfCellModemState_Type()
)
mIfCellModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellModemState.setStatus("current")


class _MIfCellRoamingState_Type(Integer32):
    """Custom type mIfCellRoamingState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("home", 1),
          ("roaming", 2))
    )


_MIfCellRoamingState_Type.__name__ = "Integer32"
_MIfCellRoamingState_Object = MibTableColumn
mIfCellRoamingState = _MIfCellRoamingState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 10),
    _MIfCellRoamingState_Type()
)
mIfCellRoamingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRoamingState.setStatus("current")


class _MIfCellServiceState_Type(Integer32):
    """Custom type mIfCellServiceState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gprs", 1),
          ("edge", 2),
          ("umts", 3),
          ("hsdpa", 4),
          ("hsupa", 5),
          ("hspaPlus", 6),
          ("is95a", 7),
          ("is95b", 8),
          ("onexRtt", 9),
          ("evdoRev0", 10),
          ("evdoReva", 11),
          ("evdoRevb", 12),
          ("evdoEhrpd", 13),
          ("lte", 14))
    )


_MIfCellServiceState_Type.__name__ = "Integer32"
_MIfCellServiceState_Object = MibTableColumn
mIfCellServiceState = _MIfCellServiceState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 11),
    _MIfCellServiceState_Type()
)
mIfCellServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellServiceState.setStatus("current")
_MIfCellRssi_Type = Integer32
_MIfCellRssi_Object = MibTableColumn
mIfCellRssi = _MIfCellRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 12),
    _MIfCellRssi_Type()
)
mIfCellRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRssi.setStatus("current")
_MIfCellRsrp_Type = Integer32
_MIfCellRsrp_Object = MibTableColumn
mIfCellRsrp = _MIfCellRsrp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 13),
    _MIfCellRsrp_Type()
)
mIfCellRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRsrp.setStatus("current")
_MIfCellRsrq_Type = Integer32
_MIfCellRsrq_Object = MibTableColumn
mIfCellRsrq = _MIfCellRsrq_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 14),
    _MIfCellRsrq_Type()
)
mIfCellRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRsrq.setStatus("current")
_MIfCellSnr_Type = Integer32
_MIfCellSnr_Object = MibTableColumn
mIfCellSnr = _MIfCellSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 15),
    _MIfCellSnr_Type()
)
mIfCellSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellSnr.setStatus("current")
_MIfCellEcio_Type = Integer32
_MIfCellEcio_Object = MibTableColumn
mIfCellEcio = _MIfCellEcio_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 16),
    _MIfCellEcio_Type()
)
mIfCellEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellEcio.setStatus("current")


class _MIfCellModemType_Type(Integer32):
    """Custom type mIfCellModemType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("typeUnknown", 0),
          ("typeE4VLteNaVerizon", 1),
          ("type3G1GsmGlobal", 2),
          ("typeE4xLteEmea", 3),
          ("type4GxLteNa", 4),
          ("type4GPLteNa", 5),
          ("typeEZ1LteEmea", 6),
          ("type4GyLteNaEu", 7),
          ("type4GzLteApac", 8),
          ("type4GaLteGlobal", 9),
          ("type4GbLteAmericas", 10),
          ("type4GcLteEu", 11),
          ("type4GdLteGlobal", 12))
    )


_MIfCellModemType_Type.__name__ = "Integer32"
_MIfCellModemType_Object = MibTableColumn
mIfCellModemType = _MIfCellModemType_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 17),
    _MIfCellModemType_Type()
)
mIfCellModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellModemType.setStatus("current")
_MIfCellModemPackageVersion_Type = DisplayString
_MIfCellModemPackageVersion_Object = MibTableColumn
mIfCellModemPackageVersion = _MIfCellModemPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 18),
    _MIfCellModemPackageVersion_Type()
)
mIfCellModemPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellModemPackageVersion.setStatus("current")
_MIfCellTac_Type = Integer32
_MIfCellTac_Object = MibTableColumn
mIfCellTac = _MIfCellTac_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 19),
    _MIfCellTac_Type()
)
mIfCellTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellTac.setStatus("current")
_MIfCellGlobalCellId_Type = Unsigned32
_MIfCellGlobalCellId_Object = MibTableColumn
mIfCellGlobalCellId = _MIfCellGlobalCellId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 20),
    _MIfCellGlobalCellId_Type()
)
mIfCellGlobalCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellGlobalCellId.setStatus("current")
_MIfCellPhysicalCellId_Type = Integer32
_MIfCellPhysicalCellId_Object = MibTableColumn
mIfCellPhysicalCellId = _MIfCellPhysicalCellId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 21),
    _MIfCellPhysicalCellId_Type()
)
mIfCellPhysicalCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellPhysicalCellId.setStatus("current")
_MIfCellBand_Type = Integer32
_MIfCellBand_Object = MibTableColumn
mIfCellBand = _MIfCellBand_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 22),
    _MIfCellBand_Type()
)
mIfCellBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellBand.setStatus("current")


class _MIfCellBandwidth_Type(Integer32):
    """Custom type mIfCellBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bwUnknown", 0),
          ("bw1dot4Mhz", 1),
          ("bw3Mhz", 2),
          ("bw5Mhz", 3),
          ("bw10Mhz", 4),
          ("bw15Mhz", 5),
          ("bw20Mhz", 6))
    )


_MIfCellBandwidth_Type.__name__ = "Integer32"
_MIfCellBandwidth_Object = MibTableColumn
mIfCellBandwidth = _MIfCellBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 23),
    _MIfCellBandwidth_Type()
)
mIfCellBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellBandwidth.setStatus("current")
_MIfCellTxChan_Type = Integer32
_MIfCellTxChan_Object = MibTableColumn
mIfCellTxChan = _MIfCellTxChan_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 24),
    _MIfCellTxChan_Type()
)
mIfCellTxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellTxChan.setStatus("current")
_MIfCellRxChan_Type = Integer32
_MIfCellRxChan_Object = MibTableColumn
mIfCellRxChan = _MIfCellRxChan_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 25),
    _MIfCellRxChan_Type()
)
mIfCellRxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRxChan.setStatus("current")


class _MIfCellEmmState_Type(Integer32):
    """Custom type mIfCellEmmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emmUnknown", 0),
          ("emmDeregistered", 1),
          ("emmRegInitiated", 2),
          ("emmRegistered", 3),
          ("emmTauInitiated", 4),
          ("emmSrInitiated", 5),
          ("emmDeregInitiated", 6),
          ("emmInvalid", 7))
    )


_MIfCellEmmState_Type.__name__ = "Integer32"
_MIfCellEmmState_Object = MibTableColumn
mIfCellEmmState = _MIfCellEmmState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 26),
    _MIfCellEmmState_Type()
)
mIfCellEmmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellEmmState.setStatus("current")


class _MIfCellRrcState_Type(Integer32):
    """Custom type mIfCellRrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rrcUnknown", 0),
          ("rrcIdle", 1),
          ("rrcWaiting", 2),
          ("rrcConnected", 3),
          ("rrcReleasing", 4))
    )


_MIfCellRrcState_Type.__name__ = "Integer32"
_MIfCellRrcState_Object = MibTableColumn
mIfCellRrcState = _MIfCellRrcState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 27),
    _MIfCellRrcState_Type()
)
mIfCellRrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellRrcState.setStatus("current")


class _MIfCellActiveSimSlot_Type(Integer32):
    """Custom type mIfCellActiveSimSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("simA", 0),
          ("simB", 1))
    )


_MIfCellActiveSimSlot_Type.__name__ = "Integer32"
_MIfCellActiveSimSlot_Object = MibTableColumn
mIfCellActiveSimSlot = _MIfCellActiveSimSlot_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 28),
    _MIfCellActiveSimSlot_Type()
)
mIfCellActiveSimSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellActiveSimSlot.setStatus("current")


class _MIfCellSimASlotState_Type(SimSlotState):
    """Custom type mIfCellSimASlotState based on SimSlotState"""
    defaultValue = 0


_MIfCellSimASlotState_Type.__name__ = "SimSlotState"
_MIfCellSimASlotState_Object = MibTableColumn
mIfCellSimASlotState = _MIfCellSimASlotState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 29),
    _MIfCellSimASlotState_Type()
)
mIfCellSimASlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellSimASlotState.setStatus("current")


class _MIfCellSimBSlotState_Type(SimSlotState):
    """Custom type mIfCellSimBSlotState based on SimSlotState"""
    defaultValue = 0


_MIfCellSimBSlotState_Type.__name__ = "SimSlotState"
_MIfCellSimBSlotState_Object = MibTableColumn
mIfCellSimBSlotState = _MIfCellSimBSlotState_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 30),
    _MIfCellSimBSlotState_Type()
)
mIfCellSimBSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellSimBSlotState.setStatus("current")
_MIfCellFwStatus_ObjectIdentity = ObjectIdentity
mIfCellFwStatus = _MIfCellFwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3)
)
_MIfCellFwStatusTable_Object = MibTable
mIfCellFwStatusTable = _MIfCellFwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mIfCellFwStatusTable.setStatus("current")
_MIfCellFwStatusEntry_Object = MibTableRow
mIfCellFwStatusEntry = _MIfCellFwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1)
)
mIfCellFwStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-CELL-MIB", "mIfCellFwId"),
)
if mibBuilder.loadTexts:
    mIfCellFwStatusEntry.setStatus("current")
_MIfCellFwId_Type = UnsignedByte
_MIfCellFwId_Object = MibTableColumn
mIfCellFwId = _MIfCellFwId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 1),
    _MIfCellFwId_Type()
)
mIfCellFwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellFwId.setStatus("current")
_MIfCellFwVersion_Type = DisplayString
_MIfCellFwVersion_Object = MibTableColumn
mIfCellFwVersion = _MIfCellFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 2),
    _MIfCellFwVersion_Type()
)
mIfCellFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellFwVersion.setStatus("current")
_MIfCellFwActive_Type = TruthValue
_MIfCellFwActive_Object = MibTableColumn
mIfCellFwActive = _MIfCellFwActive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 3),
    _MIfCellFwActive_Type()
)
mIfCellFwActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfCellFwActive.setStatus("current")
_MdsIfCellMIBConformance_ObjectIdentity = ObjectIdentity
mdsIfCellMIBConformance = _MdsIfCellMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3)
)
_MdsIfCellMIBCompliances_ObjectIdentity = ObjectIdentity
mdsIfCellMIBCompliances = _MdsIfCellMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1)
)
_MdsIfCellMIBGroups_ObjectIdentity = ObjectIdentity
mdsIfCellMIBGroups = _MdsIfCellMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2)
)

# Managed Objects groups

mIfCellStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 1)
)
mIfCellStatusGroup.setObjects(
      *(("MDS-IF-CELL-MIB", "mIfCellImsi"),
        ("MDS-IF-CELL-MIB", "mIfCellImei"),
        ("MDS-IF-CELL-MIB", "mIfCellIccid"),
        ("MDS-IF-CELL-MIB", "mIfCellMdn"),
        ("MDS-IF-CELL-MIB", "mIfCellApn"),
        ("MDS-IF-CELL-MIB", "mIfCellAppSwVersion"),
        ("MDS-IF-CELL-MIB", "mIfCellModemSwVersion"),
        ("MDS-IF-CELL-MIB", "mIfCellSimState"),
        ("MDS-IF-CELL-MIB", "mIfCellModemState"),
        ("MDS-IF-CELL-MIB", "mIfCellRoamingState"),
        ("MDS-IF-CELL-MIB", "mIfCellServiceState"),
        ("MDS-IF-CELL-MIB", "mIfCellRssi"),
        ("MDS-IF-CELL-MIB", "mIfCellRsrp"),
        ("MDS-IF-CELL-MIB", "mIfCellRsrq"),
        ("MDS-IF-CELL-MIB", "mIfCellSnr"),
        ("MDS-IF-CELL-MIB", "mIfCellEcio"),
        ("MDS-IF-CELL-MIB", "mIfCellModemType"),
        ("MDS-IF-CELL-MIB", "mIfCellModemPackageVersion"),
        ("MDS-IF-CELL-MIB", "mIfCellTac"),
        ("MDS-IF-CELL-MIB", "mIfCellGlobalCellId"),
        ("MDS-IF-CELL-MIB", "mIfCellPhysicalCellId"),
        ("MDS-IF-CELL-MIB", "mIfCellBand"),
        ("MDS-IF-CELL-MIB", "mIfCellBandwidth"),
        ("MDS-IF-CELL-MIB", "mIfCellTxChan"),
        ("MDS-IF-CELL-MIB", "mIfCellRxChan"),
        ("MDS-IF-CELL-MIB", "mIfCellEmmState"),
        ("MDS-IF-CELL-MIB", "mIfCellRrcState"),
        ("MDS-IF-CELL-MIB", "mIfCellActiveSimSlot"),
        ("MDS-IF-CELL-MIB", "mIfCellSimASlotState"),
        ("MDS-IF-CELL-MIB", "mIfCellSimBSlotState"))
)
if mibBuilder.loadTexts:
    mIfCellStatusGroup.setStatus("current")

mIfCellFwStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 2)
)
mIfCellFwStatusGroup.setObjects(
      *(("MDS-IF-CELL-MIB", "mIfCellFwId"),
        ("MDS-IF-CELL-MIB", "mIfCellFwVersion"),
        ("MDS-IF-CELL-MIB", "mIfCellFwActive"))
)
if mibBuilder.loadTexts:
    mIfCellFwStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mIfCellCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1, 1)
)
mIfCellCompliance.setObjects(
      *(("MDS-IF-CELL-MIB", "mIfCellStatusGroup"),
        ("MDS-IF-CELL-MIB", "mIfCellFwStatusGroup"))
)
if mibBuilder.loadTexts:
    mIfCellCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-IF-CELL-MIB",
    **{"UnsignedByte": UnsignedByte,
       "SimSlotState": SimSlotState,
       "mdsIfCellMIB": mdsIfCellMIB,
       "mIfCellMIBObjects": mIfCellMIBObjects,
       "mIfCellConfig": mIfCellConfig,
       "mIfCellStatus": mIfCellStatus,
       "mIfCellStatusTable": mIfCellStatusTable,
       "mIfCellStatusEntry": mIfCellStatusEntry,
       "mIfCellImsi": mIfCellImsi,
       "mIfCellImei": mIfCellImei,
       "mIfCellIccid": mIfCellIccid,
       "mIfCellMdn": mIfCellMdn,
       "mIfCellApn": mIfCellApn,
       "mIfCellAppSwVersion": mIfCellAppSwVersion,
       "mIfCellModemSwVersion": mIfCellModemSwVersion,
       "mIfCellSimState": mIfCellSimState,
       "mIfCellModemState": mIfCellModemState,
       "mIfCellRoamingState": mIfCellRoamingState,
       "mIfCellServiceState": mIfCellServiceState,
       "mIfCellRssi": mIfCellRssi,
       "mIfCellRsrp": mIfCellRsrp,
       "mIfCellRsrq": mIfCellRsrq,
       "mIfCellSnr": mIfCellSnr,
       "mIfCellEcio": mIfCellEcio,
       "mIfCellModemType": mIfCellModemType,
       "mIfCellModemPackageVersion": mIfCellModemPackageVersion,
       "mIfCellTac": mIfCellTac,
       "mIfCellGlobalCellId": mIfCellGlobalCellId,
       "mIfCellPhysicalCellId": mIfCellPhysicalCellId,
       "mIfCellBand": mIfCellBand,
       "mIfCellBandwidth": mIfCellBandwidth,
       "mIfCellTxChan": mIfCellTxChan,
       "mIfCellRxChan": mIfCellRxChan,
       "mIfCellEmmState": mIfCellEmmState,
       "mIfCellRrcState": mIfCellRrcState,
       "mIfCellActiveSimSlot": mIfCellActiveSimSlot,
       "mIfCellSimASlotState": mIfCellSimASlotState,
       "mIfCellSimBSlotState": mIfCellSimBSlotState,
       "mIfCellFwStatus": mIfCellFwStatus,
       "mIfCellFwStatusTable": mIfCellFwStatusTable,
       "mIfCellFwStatusEntry": mIfCellFwStatusEntry,
       "mIfCellFwId": mIfCellFwId,
       "mIfCellFwVersion": mIfCellFwVersion,
       "mIfCellFwActive": mIfCellFwActive,
       "mdsIfCellMIBConformance": mdsIfCellMIBConformance,
       "mdsIfCellMIBCompliances": mdsIfCellMIBCompliances,
       "mIfCellCompliance": mIfCellCompliance,
       "mdsIfCellMIBGroups": mdsIfCellMIBGroups,
       "mIfCellStatusGroup": mIfCellStatusGroup,
       "mIfCellFwStatusGroup": mIfCellFwStatusGroup}
)
