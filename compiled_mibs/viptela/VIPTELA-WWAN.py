# SNMP MIB module (VIPTELA-WWAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-WWAN
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:11 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_wwan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 16)
)
if mibBuilder.loadTexts:
    viptela_wwan.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Byte(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Short(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class WwanAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pAP", 1),
          ("cHAP", 2),
          ("pAP-CHAP", 3))
    )



class WwanPdnType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 0),
          ("iPv6", 2),
          ("iPv46", 3))
    )



class WwanRegistrationStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("not-registered", 0),
          ("registered", 1),
          ("searching", 2),
          ("registration-denied", 3),
          ("unknown", 4))
    )



class WwanRadioEnum(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("no-service", 0),
          ("aMPS", 1),
          ("cDMA", 2),
          ("gSM", 3),
          ("hDR", 4),
          ("wCDMA", 5),
          ("gPS", 6),
          ("not-used", 7),
          ("wLAN", 8),
          ("lTE", 9))
    )



class WwanActivationEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-activated", 0),
          ("activated", 1),
          ("not-applicable", 2))
    )



class WwanQosEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("modified", 2),
          ("deleted", 3),
          ("suspended", 4),
          ("enabled", 5),
          ("disabled", 6))
    )



class WwanStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Cellular_ObjectIdentity = ObjectIdentity
cellular = _Cellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1)
)
_CellularRadioTable_Object = MibTable
cellularRadioTable = _CellularRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1)
)
if mibBuilder.loadTexts:
    cellularRadioTable.setStatus("current")
_CellularRadioEntry_Object = MibTableRow
cellularRadioEntry = _CellularRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1)
)
cellularRadioEntry.setIndexNames(
    (1, "VIPTELA-WWAN", "cellularRadioIfName"),
)
if mibBuilder.loadTexts:
    cellularRadioEntry.setStatus("current")


class _CellularRadioIfName_Type(String):
    """Custom type cellularRadioIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularRadioIfName_Type.__name__ = "String"
_CellularRadioIfName_Object = MibTableColumn
cellularRadioIfName = _CellularRadioIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 1),
    _CellularRadioIfName_Type()
)
cellularRadioIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularRadioIfName.setStatus("current")
_CellularRadioBand_Type = UnsignedByte
_CellularRadioBand_Object = MibTableColumn
cellularRadioBand = _CellularRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 2),
    _CellularRadioBand_Type()
)
cellularRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioBand.setStatus("current")
_CellularRadioBandwidth_Type = ConfdString
_CellularRadioBandwidth_Object = MibTableColumn
cellularRadioBandwidth = _CellularRadioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 3),
    _CellularRadioBandwidth_Type()
)
cellularRadioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioBandwidth.setStatus("current")
_CellularRadioTxChannel_Type = UnsignedShort
_CellularRadioTxChannel_Object = MibTableColumn
cellularRadioTxChannel = _CellularRadioTxChannel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 4),
    _CellularRadioTxChannel_Type()
)
cellularRadioTxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioTxChannel.setStatus("current")
_CellularRadioRxChannel_Type = UnsignedShort
_CellularRadioRxChannel_Object = MibTableColumn
cellularRadioRxChannel = _CellularRadioRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 5),
    _CellularRadioRxChannel_Type()
)
cellularRadioRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRxChannel.setStatus("current")
_CellularRadioRssi_Type = Byte
_CellularRadioRssi_Object = MibTableColumn
cellularRadioRssi = _CellularRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 6),
    _CellularRadioRssi_Type()
)
cellularRadioRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRssi.setStatus("current")
_CellularRadioRsrp_Type = Short
_CellularRadioRsrp_Object = MibTableColumn
cellularRadioRsrp = _CellularRadioRsrp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 7),
    _CellularRadioRsrp_Type()
)
cellularRadioRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRsrp.setStatus("current")


class _CellularRadioRsrpComment_Type(String):
    """Custom type cellularRadioRsrpComment based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularRadioRsrpComment_Type.__name__ = "String"
_CellularRadioRsrpComment_Object = MibTableColumn
cellularRadioRsrpComment = _CellularRadioRsrpComment_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 8),
    _CellularRadioRsrpComment_Type()
)
cellularRadioRsrpComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRsrpComment.setStatus("current")
_CellularRadioRsrq_Type = Byte
_CellularRadioRsrq_Object = MibTableColumn
cellularRadioRsrq = _CellularRadioRsrq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 9),
    _CellularRadioRsrq_Type()
)
cellularRadioRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRsrq.setStatus("current")


class _CellularRadioRsrqComment_Type(String):
    """Custom type cellularRadioRsrqComment based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularRadioRsrqComment_Type.__name__ = "String"
_CellularRadioRsrqComment_Object = MibTableColumn
cellularRadioRsrqComment = _CellularRadioRsrqComment_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 10),
    _CellularRadioRsrqComment_Type()
)
cellularRadioRsrqComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioRsrqComment.setStatus("current")
_CellularRadioSnr_Type = ConfdString
_CellularRadioSnr_Object = MibTableColumn
cellularRadioSnr = _CellularRadioSnr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 11),
    _CellularRadioSnr_Type()
)
cellularRadioSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioSnr.setStatus("current")


class _CellularRadioSnrComment_Type(String):
    """Custom type cellularRadioSnrComment based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularRadioSnrComment_Type.__name__ = "String"
_CellularRadioSnrComment_Object = MibTableColumn
cellularRadioSnrComment = _CellularRadioSnrComment_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 12),
    _CellularRadioSnrComment_Type()
)
cellularRadioSnrComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioSnrComment.setStatus("current")
_CellularRadioEcio_Type = ConfdString
_CellularRadioEcio_Object = MibTableColumn
cellularRadioEcio = _CellularRadioEcio_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 13),
    _CellularRadioEcio_Type()
)
cellularRadioEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioEcio.setStatus("current")
_CellularRadioSinr_Type = ConfdString
_CellularRadioSinr_Object = MibTableColumn
cellularRadioSinr = _CellularRadioSinr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 14),
    _CellularRadioSinr_Type()
)
cellularRadioSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioSinr.setStatus("current")
_CellularRadioIo_Type = Integer32
_CellularRadioIo_Object = MibTableColumn
cellularRadioIo = _CellularRadioIo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 15),
    _CellularRadioIo_Type()
)
cellularRadioIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioIo.setStatus("current")
_CellularRadioMode_Type = WwanRadioEnum
_CellularRadioMode_Object = MibTableColumn
cellularRadioMode = _CellularRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 16),
    _CellularRadioMode_Type()
)
cellularRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioMode.setStatus("current")


class _CellularRadioBandClass_Type(String):
    """Custom type cellularRadioBandClass based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CellularRadioBandClass_Type.__name__ = "String"
_CellularRadioBandClass_Object = MibTableColumn
cellularRadioBandClass = _CellularRadioBandClass_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 17),
    _CellularRadioBandClass_Type()
)
cellularRadioBandClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioBandClass.setStatus("current")
_CellularRadioChannel_Type = UnsignedShort
_CellularRadioChannel_Object = MibTableColumn
cellularRadioChannel = _CellularRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 1, 1, 18),
    _CellularRadioChannel_Type()
)
cellularRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularRadioChannel.setStatus("current")
_CellularSessionsTable_Object = MibTable
cellularSessionsTable = _CellularSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2)
)
if mibBuilder.loadTexts:
    cellularSessionsTable.setStatus("current")
_CellularSessionsEntry_Object = MibTableRow
cellularSessionsEntry = _CellularSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1)
)
cellularSessionsEntry.setIndexNames(
    (0, "VIPTELA-WWAN", "cellularSessionsIfName"),
    (0, "VIPTELA-WWAN", "cellularSessionsSessionId"),
)
if mibBuilder.loadTexts:
    cellularSessionsEntry.setStatus("current")


class _CellularSessionsIfName_Type(String):
    """Custom type cellularSessionsIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularSessionsIfName_Type.__name__ = "String"
_CellularSessionsIfName_Object = MibTableColumn
cellularSessionsIfName = _CellularSessionsIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 1),
    _CellularSessionsIfName_Type()
)
cellularSessionsIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularSessionsIfName.setStatus("current")
_CellularSessionsSessionId_Type = UnsignedByte
_CellularSessionsSessionId_Object = MibTableColumn
cellularSessionsSessionId = _CellularSessionsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 2),
    _CellularSessionsSessionId_Type()
)
cellularSessionsSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularSessionsSessionId.setStatus("current")


class _CellularSessionsDataBearer_Type(String):
    """Custom type cellularSessionsDataBearer based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularSessionsDataBearer_Type.__name__ = "String"
_CellularSessionsDataBearer_Object = MibTableColumn
cellularSessionsDataBearer = _CellularSessionsDataBearer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 3),
    _CellularSessionsDataBearer_Type()
)
cellularSessionsDataBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsDataBearer.setStatus("current")


class _CellularSessionsDormancyState_Type(String):
    """Custom type cellularSessionsDormancyState based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularSessionsDormancyState_Type.__name__ = "String"
_CellularSessionsDormancyState_Object = MibTableColumn
cellularSessionsDormancyState = _CellularSessionsDormancyState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 4),
    _CellularSessionsDormancyState_Type()
)
cellularSessionsDormancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsDormancyState.setStatus("current")


class _CellularSessionsActiveProfile_Type(UnsignedByte):
    """Custom type cellularSessionsActiveProfile based on UnsignedByte"""
    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CellularSessionsActiveProfile_Type.__name__ = "UnsignedByte"
_CellularSessionsActiveProfile_Object = MibTableColumn
cellularSessionsActiveProfile = _CellularSessionsActiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 5),
    _CellularSessionsActiveProfile_Type()
)
cellularSessionsActiveProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsActiveProfile.setStatus("current")
_CellularSessionsRxPackets_Type = Counter64
_CellularSessionsRxPackets_Object = MibTableColumn
cellularSessionsRxPackets = _CellularSessionsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 6),
    _CellularSessionsRxPackets_Type()
)
cellularSessionsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsRxPackets.setStatus("current")
_CellularSessionsRxDrops_Type = Counter64
_CellularSessionsRxDrops_Object = MibTableColumn
cellularSessionsRxDrops = _CellularSessionsRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 7),
    _CellularSessionsRxDrops_Type()
)
cellularSessionsRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsRxDrops.setStatus("current")
_CellularSessionsRxErrors_Type = Counter64
_CellularSessionsRxErrors_Object = MibTableColumn
cellularSessionsRxErrors = _CellularSessionsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 8),
    _CellularSessionsRxErrors_Type()
)
cellularSessionsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsRxErrors.setStatus("current")
_CellularSessionsRxOverflows_Type = Counter64
_CellularSessionsRxOverflows_Object = MibTableColumn
cellularSessionsRxOverflows = _CellularSessionsRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 9),
    _CellularSessionsRxOverflows_Type()
)
cellularSessionsRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsRxOverflows.setStatus("current")
_CellularSessionsTxPackets_Type = Counter64
_CellularSessionsTxPackets_Object = MibTableColumn
cellularSessionsTxPackets = _CellularSessionsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 10),
    _CellularSessionsTxPackets_Type()
)
cellularSessionsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsTxPackets.setStatus("current")
_CellularSessionsTxDrops_Type = Counter64
_CellularSessionsTxDrops_Object = MibTableColumn
cellularSessionsTxDrops = _CellularSessionsTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 11),
    _CellularSessionsTxDrops_Type()
)
cellularSessionsTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsTxDrops.setStatus("current")
_CellularSessionsTxErrors_Type = Counter64
_CellularSessionsTxErrors_Object = MibTableColumn
cellularSessionsTxErrors = _CellularSessionsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 12),
    _CellularSessionsTxErrors_Type()
)
cellularSessionsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsTxErrors.setStatus("current")
_CellularSessionsTxOverflows_Type = Counter64
_CellularSessionsTxOverflows_Object = MibTableColumn
cellularSessionsTxOverflows = _CellularSessionsTxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 13),
    _CellularSessionsTxOverflows_Type()
)
cellularSessionsTxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsTxOverflows.setStatus("current")
_CellularSessionsRxOctets_Type = Counter64
_CellularSessionsRxOctets_Object = MibTableColumn
cellularSessionsRxOctets = _CellularSessionsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 14),
    _CellularSessionsRxOctets_Type()
)
cellularSessionsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsRxOctets.setStatus("current")
_CellularSessionsTxOctets_Type = Counter64
_CellularSessionsTxOctets_Object = MibTableColumn
cellularSessionsTxOctets = _CellularSessionsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 15),
    _CellularSessionsTxOctets_Type()
)
cellularSessionsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsTxOctets.setStatus("current")
_CellularSessionsIpv4Addr_Type = IpAddress
_CellularSessionsIpv4Addr_Object = MibTableColumn
cellularSessionsIpv4Addr = _CellularSessionsIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 16),
    _CellularSessionsIpv4Addr_Type()
)
cellularSessionsIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsIpv4Addr.setStatus("current")
_CellularSessionsIpv4Mask_Type = UnsignedByte
_CellularSessionsIpv4Mask_Object = MibTableColumn
cellularSessionsIpv4Mask = _CellularSessionsIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 17),
    _CellularSessionsIpv4Mask_Type()
)
cellularSessionsIpv4Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsIpv4Mask.setStatus("current")
_CellularSessionsIpv4Gw_Type = IpAddress
_CellularSessionsIpv4Gw_Object = MibTableColumn
cellularSessionsIpv4Gw = _CellularSessionsIpv4Gw_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 18),
    _CellularSessionsIpv4Gw_Type()
)
cellularSessionsIpv4Gw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsIpv4Gw.setStatus("current")
_CellularSessionsIpv4DnsPri_Type = IpAddress
_CellularSessionsIpv4DnsPri_Object = MibTableColumn
cellularSessionsIpv4DnsPri = _CellularSessionsIpv4DnsPri_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 19),
    _CellularSessionsIpv4DnsPri_Type()
)
cellularSessionsIpv4DnsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsIpv4DnsPri.setStatus("current")
_CellularSessionsIpv4DnsSec_Type = IpAddress
_CellularSessionsIpv4DnsSec_Object = MibTableColumn
cellularSessionsIpv4DnsSec = _CellularSessionsIpv4DnsSec_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 20),
    _CellularSessionsIpv4DnsSec_Type()
)
cellularSessionsIpv4DnsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsIpv4DnsSec.setStatus("current")
_CellularSessionsUptime_Type = String
_CellularSessionsUptime_Object = MibTableColumn
cellularSessionsUptime = _CellularSessionsUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 2, 1, 21),
    _CellularSessionsUptime_Type()
)
cellularSessionsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularSessionsUptime.setStatus("current")
_CellularNetworkTable_Object = MibTable
cellularNetworkTable = _CellularNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3)
)
if mibBuilder.loadTexts:
    cellularNetworkTable.setStatus("current")
_CellularNetworkEntry_Object = MibTableRow
cellularNetworkEntry = _CellularNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1)
)
cellularNetworkEntry.setIndexNames(
    (1, "VIPTELA-WWAN", "cellularNetworkIfName"),
)
if mibBuilder.loadTexts:
    cellularNetworkEntry.setStatus("current")


class _CellularNetworkIfName_Type(String):
    """Custom type cellularNetworkIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularNetworkIfName_Type.__name__ = "String"
_CellularNetworkIfName_Object = MibTableColumn
cellularNetworkIfName = _CellularNetworkIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 1),
    _CellularNetworkIfName_Type()
)
cellularNetworkIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularNetworkIfName.setStatus("current")
_CellularNetworkRegStatus_Type = WwanRegistrationStatus
_CellularNetworkRegStatus_Object = MibTableColumn
cellularNetworkRegStatus = _CellularNetworkRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 2),
    _CellularNetworkRegStatus_Type()
)
cellularNetworkRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkRegStatus.setStatus("current")


class _CellularNetworkRoamStatus_Type(String):
    """Custom type cellularNetworkRoamStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkRoamStatus_Type.__name__ = "String"
_CellularNetworkRoamStatus_Object = MibTableColumn
cellularNetworkRoamStatus = _CellularNetworkRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 3),
    _CellularNetworkRoamStatus_Type()
)
cellularNetworkRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkRoamStatus.setStatus("current")


class _CellularNetworkDomainStatus_Type(String):
    """Custom type cellularNetworkDomainStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkDomainStatus_Type.__name__ = "String"
_CellularNetworkDomainStatus_Object = MibTableColumn
cellularNetworkDomainStatus = _CellularNetworkDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 4),
    _CellularNetworkDomainStatus_Type()
)
cellularNetworkDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkDomainStatus.setStatus("current")
_CellularNetworkMcc_Type = UnsignedShort
_CellularNetworkMcc_Object = MibTableColumn
cellularNetworkMcc = _CellularNetworkMcc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 5),
    _CellularNetworkMcc_Type()
)
cellularNetworkMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkMcc.setStatus("current")
_CellularNetworkMnc_Type = UnsignedShort
_CellularNetworkMnc_Object = MibTableColumn
cellularNetworkMnc = _CellularNetworkMnc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 6),
    _CellularNetworkMnc_Type()
)
cellularNetworkMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkMnc.setStatus("current")


class _CellularNetworkNwName_Type(String):
    """Custom type cellularNetworkNwName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkNwName_Type.__name__ = "String"
_CellularNetworkNwName_Object = MibTableColumn
cellularNetworkNwName = _CellularNetworkNwName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 7),
    _CellularNetworkNwName_Type()
)
cellularNetworkNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkNwName.setStatus("current")


class _CellularNetworkEmmState_Type(String):
    """Custom type cellularNetworkEmmState based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkEmmState_Type.__name__ = "String"
_CellularNetworkEmmState_Object = MibTableColumn
cellularNetworkEmmState = _CellularNetworkEmmState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 8),
    _CellularNetworkEmmState_Type()
)
cellularNetworkEmmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkEmmState.setStatus("current")


class _CellularNetworkEmmSubstate_Type(String):
    """Custom type cellularNetworkEmmSubstate based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkEmmSubstate_Type.__name__ = "String"
_CellularNetworkEmmSubstate_Object = MibTableColumn
cellularNetworkEmmSubstate = _CellularNetworkEmmSubstate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 9),
    _CellularNetworkEmmSubstate_Type()
)
cellularNetworkEmmSubstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkEmmSubstate.setStatus("current")


class _CellularNetworkEmmConnstate_Type(String):
    """Custom type cellularNetworkEmmConnstate based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularNetworkEmmConnstate_Type.__name__ = "String"
_CellularNetworkEmmConnstate_Object = MibTableColumn
cellularNetworkEmmConnstate = _CellularNetworkEmmConnstate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 10),
    _CellularNetworkEmmConnstate_Type()
)
cellularNetworkEmmConnstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkEmmConnstate.setStatus("current")
_CellularNetworkCellid_Type = ConfdString
_CellularNetworkCellid_Object = MibTableColumn
cellularNetworkCellid = _CellularNetworkCellid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 11),
    _CellularNetworkCellid_Type()
)
cellularNetworkCellid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkCellid.setStatus("current")
_CellularNetworkTac_Type = UnsignedShort
_CellularNetworkTac_Object = MibTableColumn
cellularNetworkTac = _CellularNetworkTac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 12),
    _CellularNetworkTac_Type()
)
cellularNetworkTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkTac.setStatus("current")
_CellularNetworkLac_Type = UnsignedShort
_CellularNetworkLac_Object = MibTableColumn
cellularNetworkLac = _CellularNetworkLac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 13),
    _CellularNetworkLac_Type()
)
cellularNetworkLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkLac.setStatus("current")
_CellularNetworkRadioMode_Type = WwanRadioEnum
_CellularNetworkRadioMode_Object = MibTableColumn
cellularNetworkRadioMode = _CellularNetworkRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 14),
    _CellularNetworkRadioMode_Type()
)
cellularNetworkRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkRadioMode.setStatus("current")
_CellularNetworkBsic_Type = UnsignedByte
_CellularNetworkBsic_Object = MibTableColumn
cellularNetworkBsic = _CellularNetworkBsic_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 15),
    _CellularNetworkBsic_Type()
)
cellularNetworkBsic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkBsic.setStatus("current")
_CellularNetworkPsc_Type = UnsignedShort
_CellularNetworkPsc_Object = MibTableColumn
cellularNetworkPsc = _CellularNetworkPsc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 16),
    _CellularNetworkPsc_Type()
)
cellularNetworkPsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkPsc.setStatus("current")
_CellularNetworkSid_Type = UnsignedShort
_CellularNetworkSid_Object = MibTableColumn
cellularNetworkSid = _CellularNetworkSid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 17),
    _CellularNetworkSid_Type()
)
cellularNetworkSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkSid.setStatus("current")
_CellularNetworkNid_Type = UnsignedShort
_CellularNetworkNid_Object = MibTableColumn
cellularNetworkNid = _CellularNetworkNid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 18),
    _CellularNetworkNid_Type()
)
cellularNetworkNid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkNid.setStatus("current")
_CellularNetworkBid_Type = UnsignedShort
_CellularNetworkBid_Object = MibTableColumn
cellularNetworkBid = _CellularNetworkBid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 3, 1, 19),
    _CellularNetworkBid_Type()
)
cellularNetworkBid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularNetworkBid.setStatus("current")
_CellularModemTable_Object = MibTable
cellularModemTable = _CellularModemTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4)
)
if mibBuilder.loadTexts:
    cellularModemTable.setStatus("current")
_CellularModemEntry_Object = MibTableRow
cellularModemEntry = _CellularModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1)
)
cellularModemEntry.setIndexNames(
    (1, "VIPTELA-WWAN", "cellularModemIfName"),
)
if mibBuilder.loadTexts:
    cellularModemEntry.setStatus("current")


class _CellularModemIfName_Type(String):
    """Custom type cellularModemIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularModemIfName_Type.__name__ = "String"
_CellularModemIfName_Object = MibTableColumn
cellularModemIfName = _CellularModemIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 1),
    _CellularModemIfName_Type()
)
cellularModemIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularModemIfName.setStatus("current")


class _CellularModemModel_Type(String):
    """Custom type cellularModemModel based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemModel_Type.__name__ = "String"
_CellularModemModel_Object = MibTableColumn
cellularModemModel = _CellularModemModel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 2),
    _CellularModemModel_Type()
)
cellularModemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemModel.setStatus("current")


class _CellularModemFwVersion_Type(String):
    """Custom type cellularModemFwVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemFwVersion_Type.__name__ = "String"
_CellularModemFwVersion_Object = MibTableColumn
cellularModemFwVersion = _CellularModemFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 3),
    _CellularModemFwVersion_Type()
)
cellularModemFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwVersion.setStatus("current")


class _CellularModemFwDate_Type(String):
    """Custom type cellularModemFwDate based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemFwDate_Type.__name__ = "String"
_CellularModemFwDate_Object = MibTableColumn
cellularModemFwDate = _CellularModemFwDate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 4),
    _CellularModemFwDate_Type()
)
cellularModemFwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwDate.setStatus("current")


class _CellularModemFwTime_Type(String):
    """Custom type cellularModemFwTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemFwTime_Type.__name__ = "String"
_CellularModemFwTime_Object = MibTableColumn
cellularModemFwTime = _CellularModemFwTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 5),
    _CellularModemFwTime_Type()
)
cellularModemFwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwTime.setStatus("current")


class _CellularModemFwPkgVer_Type(String):
    """Custom type cellularModemFwPkgVer based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularModemFwPkgVer_Type.__name__ = "String"
_CellularModemFwPkgVer_Object = MibTableColumn
cellularModemFwPkgVer = _CellularModemFwPkgVer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 6),
    _CellularModemFwPkgVer_Type()
)
cellularModemFwPkgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwPkgVer.setStatus("current")


class _CellularModemFwPkgCarrier_Type(String):
    """Custom type cellularModemFwPkgCarrier based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularModemFwPkgCarrier_Type.__name__ = "String"
_CellularModemFwPkgCarrier_Object = MibTableColumn
cellularModemFwPkgCarrier = _CellularModemFwPkgCarrier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 7),
    _CellularModemFwPkgCarrier_Type()
)
cellularModemFwPkgCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwPkgCarrier.setStatus("current")


class _CellularModemFwPkgPri_Type(String):
    """Custom type cellularModemFwPkgPri based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularModemFwPkgPri_Type.__name__ = "String"
_CellularModemFwPkgPri_Object = MibTableColumn
cellularModemFwPkgPri = _CellularModemFwPkgPri_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 8),
    _CellularModemFwPkgPri_Type()
)
cellularModemFwPkgPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwPkgPri.setStatus("current")


class _CellularModemFwPkgSubver_Type(String):
    """Custom type cellularModemFwPkgSubver based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularModemFwPkgSubver_Type.__name__ = "String"
_CellularModemFwPkgSubver_Object = MibTableColumn
cellularModemFwPkgSubver = _CellularModemFwPkgSubver_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 9),
    _CellularModemFwPkgSubver_Type()
)
cellularModemFwPkgSubver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemFwPkgSubver.setStatus("current")


class _CellularModemHwVersion_Type(String):
    """Custom type cellularModemHwVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemHwVersion_Type.__name__ = "String"
_CellularModemHwVersion_Object = MibTableColumn
cellularModemHwVersion = _CellularModemHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 10),
    _CellularModemHwVersion_Type()
)
cellularModemHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemHwVersion.setStatus("current")


class _CellularModemModemStatus_Type(String):
    """Custom type cellularModemModemStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemModemStatus_Type.__name__ = "String"
_CellularModemModemStatus_Object = MibTableColumn
cellularModemModemStatus = _CellularModemModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 11),
    _CellularModemModemStatus_Type()
)
cellularModemModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemModemStatus.setStatus("current")
_CellularModemTemperature_Type = Byte
_CellularModemTemperature_Object = MibTableColumn
cellularModemTemperature = _CellularModemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 12),
    _CellularModemTemperature_Type()
)
cellularModemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemTemperature.setStatus("current")


class _CellularModemImsi_Type(String):
    """Custom type cellularModemImsi based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemImsi_Type.__name__ = "String"
_CellularModemImsi_Object = MibTableColumn
cellularModemImsi = _CellularModemImsi_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 13),
    _CellularModemImsi_Type()
)
cellularModemImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemImsi.setStatus("current")


class _CellularModemImei_Type(String):
    """Custom type cellularModemImei based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemImei_Type.__name__ = "String"
_CellularModemImei_Object = MibTableColumn
cellularModemImei = _CellularModemImei_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 14),
    _CellularModemImei_Type()
)
cellularModemImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemImei.setStatus("current")


class _CellularModemIccid_Type(String):
    """Custom type cellularModemIccid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemIccid_Type.__name__ = "String"
_CellularModemIccid_Object = MibTableColumn
cellularModemIccid = _CellularModemIccid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 15),
    _CellularModemIccid_Type()
)
cellularModemIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemIccid.setStatus("current")


class _CellularModemMsisdn_Type(String):
    """Custom type cellularModemMsisdn based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemMsisdn_Type.__name__ = "String"
_CellularModemMsisdn_Object = MibTableColumn
cellularModemMsisdn = _CellularModemMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 16),
    _CellularModemMsisdn_Type()
)
cellularModemMsisdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemMsisdn.setStatus("current")


class _CellularModemEsn_Type(String):
    """Custom type cellularModemEsn based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularModemEsn_Type.__name__ = "String"
_CellularModemEsn_Object = MibTableColumn
cellularModemEsn = _CellularModemEsn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 4, 1, 17),
    _CellularModemEsn_Type()
)
cellularModemEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularModemEsn.setStatus("current")
_CellularStatusTable_Object = MibTable
cellularStatusTable = _CellularStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5)
)
if mibBuilder.loadTexts:
    cellularStatusTable.setStatus("current")
_CellularStatusEntry_Object = MibTableRow
cellularStatusEntry = _CellularStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1)
)
cellularStatusEntry.setIndexNames(
    (1, "VIPTELA-WWAN", "cellularStatusIfName"),
)
if mibBuilder.loadTexts:
    cellularStatusEntry.setStatus("current")


class _CellularStatusIfName_Type(String):
    """Custom type cellularStatusIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularStatusIfName_Type.__name__ = "String"
_CellularStatusIfName_Object = MibTableColumn
cellularStatusIfName = _CellularStatusIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 1),
    _CellularStatusIfName_Type()
)
cellularStatusIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularStatusIfName.setStatus("current")


class _CellularStatusModemStatus_Type(String):
    """Custom type cellularStatusModemStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularStatusModemStatus_Type.__name__ = "String"
_CellularStatusModemStatus_Object = MibTableColumn
cellularStatusModemStatus = _CellularStatusModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 2),
    _CellularStatusModemStatus_Type()
)
cellularStatusModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusModemStatus.setStatus("current")


class _CellularStatusSimStatus_Type(String):
    """Custom type cellularStatusSimStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularStatusSimStatus_Type.__name__ = "String"
_CellularStatusSimStatus_Object = MibTableColumn
cellularStatusSimStatus = _CellularStatusSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 3),
    _CellularStatusSimStatus_Type()
)
cellularStatusSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusSimStatus.setStatus("current")
_CellularStatusRadioMode_Type = WwanRadioEnum
_CellularStatusRadioMode_Object = MibTableColumn
cellularStatusRadioMode = _CellularStatusRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 4),
    _CellularStatusRadioMode_Type()
)
cellularStatusRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusRadioMode.setStatus("current")


class _CellularStatusSignalStrength_Type(String):
    """Custom type cellularStatusSignalStrength based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CellularStatusSignalStrength_Type.__name__ = "String"
_CellularStatusSignalStrength_Object = MibTableColumn
cellularStatusSignalStrength = _CellularStatusSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 5),
    _CellularStatusSignalStrength_Type()
)
cellularStatusSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusSignalStrength.setStatus("current")
_CellularStatusNetworkStatus_Type = WwanRegistrationStatus
_CellularStatusNetworkStatus_Object = MibTableColumn
cellularStatusNetworkStatus = _CellularStatusNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 6),
    _CellularStatusNetworkStatus_Type()
)
cellularStatusNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusNetworkStatus.setStatus("current")


class _CellularStatusLastSeenError_Type(String):
    """Custom type cellularStatusLastSeenError based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_CellularStatusLastSeenError_Type.__name__ = "String"
_CellularStatusLastSeenError_Object = MibTableColumn
cellularStatusLastSeenError = _CellularStatusLastSeenError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 7),
    _CellularStatusLastSeenError_Type()
)
cellularStatusLastSeenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusLastSeenError.setStatus("current")
_CellularStatusActivationStatus_Type = WwanActivationEnum
_CellularStatusActivationStatus_Object = MibTableColumn
cellularStatusActivationStatus = _CellularStatusActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 5, 1, 8),
    _CellularStatusActivationStatus_Type()
)
cellularStatusActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularStatusActivationStatus.setStatus("current")
_CellularProfilesTable_Object = MibTable
cellularProfilesTable = _CellularProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6)
)
if mibBuilder.loadTexts:
    cellularProfilesTable.setStatus("current")
_CellularProfilesEntry_Object = MibTableRow
cellularProfilesEntry = _CellularProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1)
)
cellularProfilesEntry.setIndexNames(
    (0, "VIPTELA-WWAN", "cellularProfilesIfName"),
    (0, "VIPTELA-WWAN", "cellularProfilesProfileId"),
)
if mibBuilder.loadTexts:
    cellularProfilesEntry.setStatus("current")


class _CellularProfilesIfName_Type(String):
    """Custom type cellularProfilesIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularProfilesIfName_Type.__name__ = "String"
_CellularProfilesIfName_Object = MibTableColumn
cellularProfilesIfName = _CellularProfilesIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 1),
    _CellularProfilesIfName_Type()
)
cellularProfilesIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularProfilesIfName.setStatus("current")
_CellularProfilesProfileId_Type = UnsignedByte
_CellularProfilesProfileId_Object = MibTableColumn
cellularProfilesProfileId = _CellularProfilesProfileId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 2),
    _CellularProfilesProfileId_Type()
)
cellularProfilesProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularProfilesProfileId.setStatus("current")
_CellularProfilesPdnType_Type = WwanPdnType
_CellularProfilesPdnType_Object = MibTableColumn
cellularProfilesPdnType = _CellularProfilesPdnType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 3),
    _CellularProfilesPdnType_Type()
)
cellularProfilesPdnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesPdnType.setStatus("current")


class _CellularProfilesApn_Type(String):
    """Custom type cellularProfilesApn based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 104),
    )


_CellularProfilesApn_Type.__name__ = "String"
_CellularProfilesApn_Object = MibTableColumn
cellularProfilesApn = _CellularProfilesApn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 4),
    _CellularProfilesApn_Type()
)
cellularProfilesApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesApn.setStatus("current")


class _CellularProfilesName_Type(String):
    """Custom type cellularProfilesName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CellularProfilesName_Type.__name__ = "String"
_CellularProfilesName_Object = MibTableColumn
cellularProfilesName = _CellularProfilesName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 5),
    _CellularProfilesName_Type()
)
cellularProfilesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesName.setStatus("current")
_CellularProfilesAuth_Type = WwanAuthType
_CellularProfilesAuth_Object = MibTableColumn
cellularProfilesAuth = _CellularProfilesAuth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 6),
    _CellularProfilesAuth_Type()
)
cellularProfilesAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesAuth.setStatus("current")
_CellularProfilesIpAddr_Type = IpAddress
_CellularProfilesIpAddr_Object = MibTableColumn
cellularProfilesIpAddr = _CellularProfilesIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 7),
    _CellularProfilesIpAddr_Type()
)
cellularProfilesIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesIpAddr.setStatus("current")
_CellularProfilesPrimaryDns_Type = IpAddress
_CellularProfilesPrimaryDns_Object = MibTableColumn
cellularProfilesPrimaryDns = _CellularProfilesPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 8),
    _CellularProfilesPrimaryDns_Type()
)
cellularProfilesPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesPrimaryDns.setStatus("current")
_CellularProfilesSecondaryDns_Type = IpAddress
_CellularProfilesSecondaryDns_Object = MibTableColumn
cellularProfilesSecondaryDns = _CellularProfilesSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 9),
    _CellularProfilesSecondaryDns_Type()
)
cellularProfilesSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesSecondaryDns.setStatus("current")


class _CellularProfilesUserName_Type(String):
    """Custom type cellularProfilesUserName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_CellularProfilesUserName_Type.__name__ = "String"
_CellularProfilesUserName_Object = MibTableColumn
cellularProfilesUserName = _CellularProfilesUserName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 6, 1, 10),
    _CellularProfilesUserName_Type()
)
cellularProfilesUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularProfilesUserName.setStatus("current")
_CellularQosTable_Object = MibTable
cellularQosTable = _CellularQosTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7)
)
if mibBuilder.loadTexts:
    cellularQosTable.setStatus("current")
_CellularQosEntry_Object = MibTableRow
cellularQosEntry = _CellularQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1)
)
cellularQosEntry.setIndexNames(
    (1, "VIPTELA-WWAN", "cellularQosIfName"),
)
if mibBuilder.loadTexts:
    cellularQosEntry.setStatus("current")


class _CellularQosIfName_Type(String):
    """Custom type cellularQosIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularQosIfName_Type.__name__ = "String"
_CellularQosIfName_Object = MibTableColumn
cellularQosIfName = _CellularQosIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1, 1),
    _CellularQosIfName_Type()
)
cellularQosIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularQosIfName.setStatus("current")
_CellularQosFlowId_Type = Unsigned32
_CellularQosFlowId_Object = MibTableColumn
cellularQosFlowId = _CellularQosFlowId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1, 2),
    _CellularQosFlowId_Type()
)
cellularQosFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularQosFlowId.setStatus("current")
_CellularQosBearerId_Type = UnsignedByte
_CellularQosBearerId_Object = MibTableColumn
cellularQosBearerId = _CellularQosBearerId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1, 3),
    _CellularQosBearerId_Type()
)
cellularQosBearerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularQosBearerId.setStatus("current")
_CellularQosQci_Type = UnsignedByte
_CellularQosQci_Object = MibTableColumn
cellularQosQci = _CellularQosQci_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1, 4),
    _CellularQosQci_Type()
)
cellularQosQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularQosQci.setStatus("current")
_CellularQosBearerStatus_Type = WwanQosEnum
_CellularQosBearerStatus_Object = MibTableColumn
cellularQosBearerStatus = _CellularQosBearerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 7, 1, 5),
    _CellularQosBearerStatus_Type()
)
cellularQosBearerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularQosBearerStatus.setStatus("current")
_CellularFirmwareTable_Object = MibTable
cellularFirmwareTable = _CellularFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8)
)
if mibBuilder.loadTexts:
    cellularFirmwareTable.setStatus("current")
_CellularFirmwareEntry_Object = MibTableRow
cellularFirmwareEntry = _CellularFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1)
)
cellularFirmwareEntry.setIndexNames(
    (0, "VIPTELA-WWAN", "cellularFirmwareIfName"),
    (0, "VIPTELA-WWAN", "cellularFirmwareImageIndex"),
)
if mibBuilder.loadTexts:
    cellularFirmwareEntry.setStatus("current")


class _CellularFirmwareIfName_Type(String):
    """Custom type cellularFirmwareIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CellularFirmwareIfName_Type.__name__ = "String"
_CellularFirmwareIfName_Object = MibTableColumn
cellularFirmwareIfName = _CellularFirmwareIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 1),
    _CellularFirmwareIfName_Type()
)
cellularFirmwareIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularFirmwareIfName.setStatus("current")
_CellularFirmwareImageIndex_Type = UnsignedByte
_CellularFirmwareImageIndex_Object = MibTableColumn
cellularFirmwareImageIndex = _CellularFirmwareImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 2),
    _CellularFirmwareImageIndex_Type()
)
cellularFirmwareImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cellularFirmwareImageIndex.setStatus("current")


class _CellularFirmwareCarrier_Type(String):
    """Custom type cellularFirmwareCarrier based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularFirmwareCarrier_Type.__name__ = "String"
_CellularFirmwareCarrier_Object = MibTableColumn
cellularFirmwareCarrier = _CellularFirmwareCarrier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 3),
    _CellularFirmwareCarrier_Type()
)
cellularFirmwareCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularFirmwareCarrier.setStatus("current")


class _CellularFirmwareVersion_Type(String):
    """Custom type cellularFirmwareVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularFirmwareVersion_Type.__name__ = "String"
_CellularFirmwareVersion_Object = MibTableColumn
cellularFirmwareVersion = _CellularFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 4),
    _CellularFirmwareVersion_Type()
)
cellularFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularFirmwareVersion.setStatus("current")


class _CellularFirmwarePriVersion_Type(String):
    """Custom type cellularFirmwarePriVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CellularFirmwarePriVersion_Type.__name__ = "String"
_CellularFirmwarePriVersion_Object = MibTableColumn
cellularFirmwarePriVersion = _CellularFirmwarePriVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 5),
    _CellularFirmwarePriVersion_Type()
)
cellularFirmwarePriVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularFirmwarePriVersion.setStatus("current")
_CellularFirmwareImageStatus_Type = WwanStatusEnum
_CellularFirmwareImageStatus_Object = MibTableColumn
cellularFirmwareImageStatus = _CellularFirmwareImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 16, 1, 8, 1, 6),
    _CellularFirmwareImageStatus_Type()
)
cellularFirmwareImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellularFirmwareImageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-WWAN",
    **{"Byte": Byte,
       "UnsignedByte": UnsignedByte,
       "Short": Short,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "WwanAuthType": WwanAuthType,
       "WwanPdnType": WwanPdnType,
       "WwanRegistrationStatus": WwanRegistrationStatus,
       "WwanRadioEnum": WwanRadioEnum,
       "WwanActivationEnum": WwanActivationEnum,
       "WwanQosEnum": WwanQosEnum,
       "WwanStatusEnum": WwanStatusEnum,
       "viptela-wwan": viptela_wwan,
       "cellular": cellular,
       "cellularRadioTable": cellularRadioTable,
       "cellularRadioEntry": cellularRadioEntry,
       "cellularRadioIfName": cellularRadioIfName,
       "cellularRadioBand": cellularRadioBand,
       "cellularRadioBandwidth": cellularRadioBandwidth,
       "cellularRadioTxChannel": cellularRadioTxChannel,
       "cellularRadioRxChannel": cellularRadioRxChannel,
       "cellularRadioRssi": cellularRadioRssi,
       "cellularRadioRsrp": cellularRadioRsrp,
       "cellularRadioRsrpComment": cellularRadioRsrpComment,
       "cellularRadioRsrq": cellularRadioRsrq,
       "cellularRadioRsrqComment": cellularRadioRsrqComment,
       "cellularRadioSnr": cellularRadioSnr,
       "cellularRadioSnrComment": cellularRadioSnrComment,
       "cellularRadioEcio": cellularRadioEcio,
       "cellularRadioSinr": cellularRadioSinr,
       "cellularRadioIo": cellularRadioIo,
       "cellularRadioMode": cellularRadioMode,
       "cellularRadioBandClass": cellularRadioBandClass,
       "cellularRadioChannel": cellularRadioChannel,
       "cellularSessionsTable": cellularSessionsTable,
       "cellularSessionsEntry": cellularSessionsEntry,
       "cellularSessionsIfName": cellularSessionsIfName,
       "cellularSessionsSessionId": cellularSessionsSessionId,
       "cellularSessionsDataBearer": cellularSessionsDataBearer,
       "cellularSessionsDormancyState": cellularSessionsDormancyState,
       "cellularSessionsActiveProfile": cellularSessionsActiveProfile,
       "cellularSessionsRxPackets": cellularSessionsRxPackets,
       "cellularSessionsRxDrops": cellularSessionsRxDrops,
       "cellularSessionsRxErrors": cellularSessionsRxErrors,
       "cellularSessionsRxOverflows": cellularSessionsRxOverflows,
       "cellularSessionsTxPackets": cellularSessionsTxPackets,
       "cellularSessionsTxDrops": cellularSessionsTxDrops,
       "cellularSessionsTxErrors": cellularSessionsTxErrors,
       "cellularSessionsTxOverflows": cellularSessionsTxOverflows,
       "cellularSessionsRxOctets": cellularSessionsRxOctets,
       "cellularSessionsTxOctets": cellularSessionsTxOctets,
       "cellularSessionsIpv4Addr": cellularSessionsIpv4Addr,
       "cellularSessionsIpv4Mask": cellularSessionsIpv4Mask,
       "cellularSessionsIpv4Gw": cellularSessionsIpv4Gw,
       "cellularSessionsIpv4DnsPri": cellularSessionsIpv4DnsPri,
       "cellularSessionsIpv4DnsSec": cellularSessionsIpv4DnsSec,
       "cellularSessionsUptime": cellularSessionsUptime,
       "cellularNetworkTable": cellularNetworkTable,
       "cellularNetworkEntry": cellularNetworkEntry,
       "cellularNetworkIfName": cellularNetworkIfName,
       "cellularNetworkRegStatus": cellularNetworkRegStatus,
       "cellularNetworkRoamStatus": cellularNetworkRoamStatus,
       "cellularNetworkDomainStatus": cellularNetworkDomainStatus,
       "cellularNetworkMcc": cellularNetworkMcc,
       "cellularNetworkMnc": cellularNetworkMnc,
       "cellularNetworkNwName": cellularNetworkNwName,
       "cellularNetworkEmmState": cellularNetworkEmmState,
       "cellularNetworkEmmSubstate": cellularNetworkEmmSubstate,
       "cellularNetworkEmmConnstate": cellularNetworkEmmConnstate,
       "cellularNetworkCellid": cellularNetworkCellid,
       "cellularNetworkTac": cellularNetworkTac,
       "cellularNetworkLac": cellularNetworkLac,
       "cellularNetworkRadioMode": cellularNetworkRadioMode,
       "cellularNetworkBsic": cellularNetworkBsic,
       "cellularNetworkPsc": cellularNetworkPsc,
       "cellularNetworkSid": cellularNetworkSid,
       "cellularNetworkNid": cellularNetworkNid,
       "cellularNetworkBid": cellularNetworkBid,
       "cellularModemTable": cellularModemTable,
       "cellularModemEntry": cellularModemEntry,
       "cellularModemIfName": cellularModemIfName,
       "cellularModemModel": cellularModemModel,
       "cellularModemFwVersion": cellularModemFwVersion,
       "cellularModemFwDate": cellularModemFwDate,
       "cellularModemFwTime": cellularModemFwTime,
       "cellularModemFwPkgVer": cellularModemFwPkgVer,
       "cellularModemFwPkgCarrier": cellularModemFwPkgCarrier,
       "cellularModemFwPkgPri": cellularModemFwPkgPri,
       "cellularModemFwPkgSubver": cellularModemFwPkgSubver,
       "cellularModemHwVersion": cellularModemHwVersion,
       "cellularModemModemStatus": cellularModemModemStatus,
       "cellularModemTemperature": cellularModemTemperature,
       "cellularModemImsi": cellularModemImsi,
       "cellularModemImei": cellularModemImei,
       "cellularModemIccid": cellularModemIccid,
       "cellularModemMsisdn": cellularModemMsisdn,
       "cellularModemEsn": cellularModemEsn,
       "cellularStatusTable": cellularStatusTable,
       "cellularStatusEntry": cellularStatusEntry,
       "cellularStatusIfName": cellularStatusIfName,
       "cellularStatusModemStatus": cellularStatusModemStatus,
       "cellularStatusSimStatus": cellularStatusSimStatus,
       "cellularStatusRadioMode": cellularStatusRadioMode,
       "cellularStatusSignalStrength": cellularStatusSignalStrength,
       "cellularStatusNetworkStatus": cellularStatusNetworkStatus,
       "cellularStatusLastSeenError": cellularStatusLastSeenError,
       "cellularStatusActivationStatus": cellularStatusActivationStatus,
       "cellularProfilesTable": cellularProfilesTable,
       "cellularProfilesEntry": cellularProfilesEntry,
       "cellularProfilesIfName": cellularProfilesIfName,
       "cellularProfilesProfileId": cellularProfilesProfileId,
       "cellularProfilesPdnType": cellularProfilesPdnType,
       "cellularProfilesApn": cellularProfilesApn,
       "cellularProfilesName": cellularProfilesName,
       "cellularProfilesAuth": cellularProfilesAuth,
       "cellularProfilesIpAddr": cellularProfilesIpAddr,
       "cellularProfilesPrimaryDns": cellularProfilesPrimaryDns,
       "cellularProfilesSecondaryDns": cellularProfilesSecondaryDns,
       "cellularProfilesUserName": cellularProfilesUserName,
       "cellularQosTable": cellularQosTable,
       "cellularQosEntry": cellularQosEntry,
       "cellularQosIfName": cellularQosIfName,
       "cellularQosFlowId": cellularQosFlowId,
       "cellularQosBearerId": cellularQosBearerId,
       "cellularQosQci": cellularQosQci,
       "cellularQosBearerStatus": cellularQosBearerStatus,
       "cellularFirmwareTable": cellularFirmwareTable,
       "cellularFirmwareEntry": cellularFirmwareEntry,
       "cellularFirmwareIfName": cellularFirmwareIfName,
       "cellularFirmwareImageIndex": cellularFirmwareImageIndex,
       "cellularFirmwareCarrier": cellularFirmwareCarrier,
       "cellularFirmwareVersion": cellularFirmwareVersion,
       "cellularFirmwarePriVersion": cellularFirmwarePriVersion,
       "cellularFirmwareImageStatus": cellularFirmwareImageStatus}
)
