# SNMP MIB module (CONEL-MOBILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icr-os\CONEL-MOBILE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:20 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Mobile_ObjectIdentity = ObjectIdentity
mobile = _Mobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 4)
)


class _MobileTechnology_Type(Integer32):
    """Custom type mobileTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24,
              26,
              28,
              30,
              32)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gprs", 2),
          ("edge", 4),
          ("umts", 6),
          ("hsdpa", 8),
          ("hsupa", 10),
          ("hspa", 12),
          ("lte", 14),
          ("cdma", 16),
          ("evdo", 18),
          ("evdo0", 20),
          ("evdoA", 22),
          ("evdoB", 24),
          ("nbiot", 26),
          ("lteM", 28),
          ("nr5gNSA", 30),
          ("nr5gSA", 32))
    )


_MobileTechnology_Type.__name__ = "Integer32"
_MobileTechnology_Object = MibScalar
mobileTechnology = _MobileTechnology_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 1),
    _MobileTechnology_Type()
)
mobileTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTechnology.setStatus("current")
_MobilePLMN_Type = OctetString
_MobilePLMN_Object = MibScalar
mobilePLMN = _MobilePLMN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 2),
    _MobilePLMN_Type()
)
mobilePLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilePLMN.setStatus("current")
_MobileCell_Type = OctetString
_MobileCell_Object = MibScalar
mobileCell = _MobileCell_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 3),
    _MobileCell_Type()
)
mobileCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileCell.setStatus("current")
_MobileChannel_Type = OctetString
_MobileChannel_Object = MibScalar
mobileChannel = _MobileChannel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 4),
    _MobileChannel_Type()
)
mobileChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannel.setStatus("current")
_MobileSignalStrength_Type = Integer32
_MobileSignalStrength_Object = MibScalar
mobileSignalStrength = _MobileSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 5),
    _MobileSignalStrength_Type()
)
mobileSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrength.setStatus("current")
_MobileChannelN1_Type = OctetString
_MobileChannelN1_Object = MibScalar
mobileChannelN1 = _MobileChannelN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 6),
    _MobileChannelN1_Type()
)
mobileChannelN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannelN1.setStatus("current")
_MobileSignalStrengthN1_Type = Integer32
_MobileSignalStrengthN1_Object = MibScalar
mobileSignalStrengthN1 = _MobileSignalStrengthN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 7),
    _MobileSignalStrengthN1_Type()
)
mobileSignalStrengthN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrengthN1.setStatus("current")
_MobileChannelN2_Type = OctetString
_MobileChannelN2_Object = MibScalar
mobileChannelN2 = _MobileChannelN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 8),
    _MobileChannelN2_Type()
)
mobileChannelN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannelN2.setStatus("current")
_MobileSignalStrengthN2_Type = Integer32
_MobileSignalStrengthN2_Object = MibScalar
mobileSignalStrengthN2 = _MobileSignalStrengthN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 9),
    _MobileSignalStrengthN2_Type()
)
mobileSignalStrengthN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrengthN2.setStatus("current")
_MobileChannelN3_Type = OctetString
_MobileChannelN3_Object = MibScalar
mobileChannelN3 = _MobileChannelN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 10),
    _MobileChannelN3_Type()
)
mobileChannelN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannelN3.setStatus("current")
_MobileSignalStrengthN3_Type = Integer32
_MobileSignalStrengthN3_Object = MibScalar
mobileSignalStrengthN3 = _MobileSignalStrengthN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 11),
    _MobileSignalStrengthN3_Type()
)
mobileSignalStrengthN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrengthN3.setStatus("current")
_MobileChannelN4_Type = OctetString
_MobileChannelN4_Object = MibScalar
mobileChannelN4 = _MobileChannelN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 12),
    _MobileChannelN4_Type()
)
mobileChannelN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannelN4.setStatus("current")
_MobileSignalStrengthN4_Type = Integer32
_MobileSignalStrengthN4_Object = MibScalar
mobileSignalStrengthN4 = _MobileSignalStrengthN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 13),
    _MobileSignalStrengthN4_Type()
)
mobileSignalStrengthN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrengthN4.setStatus("current")
_MobileChannelN5_Type = OctetString
_MobileChannelN5_Object = MibScalar
mobileChannelN5 = _MobileChannelN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 14),
    _MobileChannelN5_Type()
)
mobileChannelN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileChannelN5.setStatus("current")
_MobileSignalStrengthN5_Type = Integer32
_MobileSignalStrengthN5_Object = MibScalar
mobileSignalStrengthN5 = _MobileSignalStrengthN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 15),
    _MobileSignalStrengthN5_Type()
)
mobileSignalStrengthN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalStrengthN5.setStatus("current")
_MobileUpTime_Type = TimeTicks
_MobileUpTime_Object = MibScalar
mobileUpTime = _MobileUpTime_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 16),
    _MobileUpTime_Type()
)
mobileUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileUpTime.setStatus("current")
_MobileConnect_Type = Counter32
_MobileConnect_Object = MibScalar
mobileConnect = _MobileConnect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 17),
    _MobileConnect_Type()
)
mobileConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileConnect.setStatus("current")
_MobileDisconnect_Type = Counter32
_MobileDisconnect_Object = MibScalar
mobileDisconnect = _MobileDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 18),
    _MobileDisconnect_Type()
)
mobileDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileDisconnect.setStatus("current")


class _MobileCard_Type(Integer32):
    """Custom type mobileCard based on Integer32"""
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
        *(("primary", 0),
          ("secondary", 1),
          ("tertiary", 2),
          ("quaternary", 3))
    )


_MobileCard_Type.__name__ = "Integer32"
_MobileCard_Object = MibScalar
mobileCard = _MobileCard_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 19),
    _MobileCard_Type()
)
mobileCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileCard.setStatus("current")
_MobileIPAddress_Type = IpAddress
_MobileIPAddress_Object = MibScalar
mobileIPAddress = _MobileIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 20),
    _MobileIPAddress_Type()
)
mobileIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileIPAddress.setStatus("current")
_MobileLatency_Type = Integer32
_MobileLatency_Object = MibScalar
mobileLatency = _MobileLatency_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 21),
    _MobileLatency_Type()
)
mobileLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLatency.setStatus("current")
_MobileReportPeriod_Type = Integer32
_MobileReportPeriod_Object = MibScalar
mobileReportPeriod = _MobileReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 22),
    _MobileReportPeriod_Type()
)
mobileReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileReportPeriod.setStatus("current")


class _MobileRegistration_Type(Integer32):
    """Custom type mobileRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idle", 1),
          ("search", 2),
          ("denied", 3),
          ("home", 4),
          ("foregien", 5))
    )


_MobileRegistration_Type.__name__ = "Integer32"
_MobileRegistration_Object = MibScalar
mobileRegistration = _MobileRegistration_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 23),
    _MobileRegistration_Type()
)
mobileRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileRegistration.setStatus("current")
_MobileOperator_Type = OctetString
_MobileOperator_Object = MibScalar
mobileOperator = _MobileOperator_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 24),
    _MobileOperator_Type()
)
mobileOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileOperator.setStatus("current")
_MobileLAC_Type = OctetString
_MobileLAC_Object = MibScalar
mobileLAC = _MobileLAC_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 25),
    _MobileLAC_Type()
)
mobileLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLAC.setStatus("current")
_MobileSignalQuality_Type = Integer32
_MobileSignalQuality_Object = MibScalar
mobileSignalQuality = _MobileSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 26),
    _MobileSignalQuality_Type()
)
mobileSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSignalQuality.setStatus("current")
_MobileCSQ_Type = Integer32
_MobileCSQ_Object = MibScalar
mobileCSQ = _MobileCSQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 27),
    _MobileCSQ_Type()
)
mobileCSQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileCSQ.setStatus("current")
_MobilePNOffset_Type = Integer32
_MobilePNOffset_Object = MibScalar
mobilePNOffset = _MobilePNOffset_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 28),
    _MobilePNOffset_Type()
)
mobilePNOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilePNOffset.setStatus("current")
_MobileBand_Type = OctetString
_MobileBand_Object = MibScalar
mobileBand = _MobileBand_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 29),
    _MobileBand_Type()
)
mobileBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileBand.setStatus("current")
_MobileRSSI_Type = Integer32
_MobileRSSI_Object = MibScalar
mobileRSSI = _MobileRSSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 30),
    _MobileRSSI_Type()
)
mobileRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileRSSI.setStatus("current")
_MobileRSCP_Type = Integer32
_MobileRSCP_Object = MibScalar
mobileRSCP = _MobileRSCP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 31),
    _MobileRSCP_Type()
)
mobileRSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileRSCP.setStatus("current")
_MobileRSRP_Type = Integer32
_MobileRSRP_Object = MibScalar
mobileRSRP = _MobileRSRP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 32),
    _MobileRSRP_Type()
)
mobileRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileRSRP.setStatus("current")
_MobileRSRQ_Type = Integer32
_MobileRSRQ_Object = MibScalar
mobileRSRQ = _MobileRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 33),
    _MobileRSRQ_Type()
)
mobileRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileRSRQ.setStatus("current")
_MobileEcIo_Type = Integer32
_MobileEcIo_Object = MibScalar
mobileEcIo = _MobileEcIo_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 34),
    _MobileEcIo_Type()
)
mobileEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileEcIo.setStatus("current")
_MobileNRBand_Type = OctetString
_MobileNRBand_Object = MibScalar
mobileNRBand = _MobileNRBand_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 35),
    _MobileNRBand_Type()
)
mobileNRBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRBand.setStatus("current")
_MobileNRChannel_Type = Integer32
_MobileNRChannel_Object = MibScalar
mobileNRChannel = _MobileNRChannel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 36),
    _MobileNRChannel_Type()
)
mobileNRChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRChannel.setStatus("current")
_MobileNRRSSI_Type = Integer32
_MobileNRRSSI_Object = MibScalar
mobileNRRSSI = _MobileNRRSSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 37),
    _MobileNRRSSI_Type()
)
mobileNRRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRRSSI.setStatus("current")
_MobileNRRSRP_Type = Integer32
_MobileNRRSRP_Object = MibScalar
mobileNRRSRP = _MobileNRRSRP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 38),
    _MobileNRRSRP_Type()
)
mobileNRRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRRSRP.setStatus("current")
_MobileNRRSRQ_Type = Integer32
_MobileNRRSRQ_Object = MibScalar
mobileNRRSRQ = _MobileNRRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 39),
    _MobileNRRSRQ_Type()
)
mobileNRRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRRSRQ.setStatus("current")
_MobileNRSINR_Type = Integer32
_MobileNRSINR_Object = MibScalar
mobileNRSINR = _MobileNRSINR_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 40),
    _MobileNRSINR_Type()
)
mobileNRSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileNRSINR.setStatus("current")
_MobileSINR_Type = Integer32
_MobileSINR_Object = MibScalar
mobileSINR = _MobileSINR_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 41),
    _MobileSINR_Type()
)
mobileSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileSINR.setStatus("current")


class _Mobile2Technology_Type(Integer32):
    """Custom type mobile2Technology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24,
              26,
              28,
              30,
              32)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gprs", 2),
          ("edge", 4),
          ("umts", 6),
          ("hsdpa", 8),
          ("hsupa", 10),
          ("hspa", 12),
          ("lte", 14),
          ("cdma", 16),
          ("evdo", 18),
          ("evdo0", 20),
          ("evdoA", 22),
          ("evdoB", 24),
          ("nbiot", 26),
          ("lteM", 28),
          ("nr5gNSA", 30),
          ("nr5gSA", 32))
    )


_Mobile2Technology_Type.__name__ = "Integer32"
_Mobile2Technology_Object = MibScalar
mobile2Technology = _Mobile2Technology_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 101),
    _Mobile2Technology_Type()
)
mobile2Technology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Technology.setStatus("current")
_Mobile2PLMN_Type = OctetString
_Mobile2PLMN_Object = MibScalar
mobile2PLMN = _Mobile2PLMN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 102),
    _Mobile2PLMN_Type()
)
mobile2PLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2PLMN.setStatus("current")
_Mobile2Cell_Type = OctetString
_Mobile2Cell_Object = MibScalar
mobile2Cell = _Mobile2Cell_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 103),
    _Mobile2Cell_Type()
)
mobile2Cell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Cell.setStatus("current")
_Mobile2Channel_Type = OctetString
_Mobile2Channel_Object = MibScalar
mobile2Channel = _Mobile2Channel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 104),
    _Mobile2Channel_Type()
)
mobile2Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Channel.setStatus("current")
_Mobile2SignalStrength_Type = Integer32
_Mobile2SignalStrength_Object = MibScalar
mobile2SignalStrength = _Mobile2SignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 105),
    _Mobile2SignalStrength_Type()
)
mobile2SignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrength.setStatus("current")
_Mobile2ChannelN1_Type = OctetString
_Mobile2ChannelN1_Object = MibScalar
mobile2ChannelN1 = _Mobile2ChannelN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 106),
    _Mobile2ChannelN1_Type()
)
mobile2ChannelN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ChannelN1.setStatus("current")
_Mobile2SignalStrengthN1_Type = Integer32
_Mobile2SignalStrengthN1_Object = MibScalar
mobile2SignalStrengthN1 = _Mobile2SignalStrengthN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 107),
    _Mobile2SignalStrengthN1_Type()
)
mobile2SignalStrengthN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrengthN1.setStatus("current")
_Mobile2ChannelN2_Type = OctetString
_Mobile2ChannelN2_Object = MibScalar
mobile2ChannelN2 = _Mobile2ChannelN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 108),
    _Mobile2ChannelN2_Type()
)
mobile2ChannelN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ChannelN2.setStatus("current")
_Mobile2SignalStrengthN2_Type = Integer32
_Mobile2SignalStrengthN2_Object = MibScalar
mobile2SignalStrengthN2 = _Mobile2SignalStrengthN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 109),
    _Mobile2SignalStrengthN2_Type()
)
mobile2SignalStrengthN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrengthN2.setStatus("current")
_Mobile2ChannelN3_Type = OctetString
_Mobile2ChannelN3_Object = MibScalar
mobile2ChannelN3 = _Mobile2ChannelN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 110),
    _Mobile2ChannelN3_Type()
)
mobile2ChannelN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ChannelN3.setStatus("current")
_Mobile2SignalStrengthN3_Type = Integer32
_Mobile2SignalStrengthN3_Object = MibScalar
mobile2SignalStrengthN3 = _Mobile2SignalStrengthN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 111),
    _Mobile2SignalStrengthN3_Type()
)
mobile2SignalStrengthN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrengthN3.setStatus("current")
_Mobile2ChannelN4_Type = OctetString
_Mobile2ChannelN4_Object = MibScalar
mobile2ChannelN4 = _Mobile2ChannelN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 112),
    _Mobile2ChannelN4_Type()
)
mobile2ChannelN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ChannelN4.setStatus("current")
_Mobile2SignalStrengthN4_Type = Integer32
_Mobile2SignalStrengthN4_Object = MibScalar
mobile2SignalStrengthN4 = _Mobile2SignalStrengthN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 113),
    _Mobile2SignalStrengthN4_Type()
)
mobile2SignalStrengthN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrengthN4.setStatus("current")
_Mobile2ChannelN5_Type = OctetString
_Mobile2ChannelN5_Object = MibScalar
mobile2ChannelN5 = _Mobile2ChannelN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 114),
    _Mobile2ChannelN5_Type()
)
mobile2ChannelN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ChannelN5.setStatus("current")
_Mobile2SignalStrengthN5_Type = Integer32
_Mobile2SignalStrengthN5_Object = MibScalar
mobile2SignalStrengthN5 = _Mobile2SignalStrengthN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 115),
    _Mobile2SignalStrengthN5_Type()
)
mobile2SignalStrengthN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalStrengthN5.setStatus("current")
_Mobile2UpTime_Type = TimeTicks
_Mobile2UpTime_Object = MibScalar
mobile2UpTime = _Mobile2UpTime_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 116),
    _Mobile2UpTime_Type()
)
mobile2UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2UpTime.setStatus("current")
_Mobile2Connect_Type = Counter32
_Mobile2Connect_Object = MibScalar
mobile2Connect = _Mobile2Connect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 117),
    _Mobile2Connect_Type()
)
mobile2Connect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Connect.setStatus("current")
_Mobile2Disconnect_Type = Counter32
_Mobile2Disconnect_Object = MibScalar
mobile2Disconnect = _Mobile2Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 118),
    _Mobile2Disconnect_Type()
)
mobile2Disconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Disconnect.setStatus("current")


class _Mobile2Card_Type(Integer32):
    """Custom type mobile2Card based on Integer32"""
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
        *(("primary", 0),
          ("secondary", 1),
          ("tertiary", 2),
          ("quaternary", 3))
    )


_Mobile2Card_Type.__name__ = "Integer32"
_Mobile2Card_Object = MibScalar
mobile2Card = _Mobile2Card_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 119),
    _Mobile2Card_Type()
)
mobile2Card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Card.setStatus("current")
_Mobile2IPAddress_Type = IpAddress
_Mobile2IPAddress_Object = MibScalar
mobile2IPAddress = _Mobile2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 120),
    _Mobile2IPAddress_Type()
)
mobile2IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2IPAddress.setStatus("current")
_Mobile2Latency_Type = Integer32
_Mobile2Latency_Object = MibScalar
mobile2Latency = _Mobile2Latency_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 121),
    _Mobile2Latency_Type()
)
mobile2Latency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Latency.setStatus("current")
_Mobile2ReportPeriod_Type = Integer32
_Mobile2ReportPeriod_Object = MibScalar
mobile2ReportPeriod = _Mobile2ReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 122),
    _Mobile2ReportPeriod_Type()
)
mobile2ReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ReportPeriod.setStatus("current")


class _Mobile2Registration_Type(Integer32):
    """Custom type mobile2Registration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idle", 1),
          ("search", 2),
          ("denied", 3),
          ("home", 4),
          ("foregien", 5))
    )


_Mobile2Registration_Type.__name__ = "Integer32"
_Mobile2Registration_Object = MibScalar
mobile2Registration = _Mobile2Registration_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 123),
    _Mobile2Registration_Type()
)
mobile2Registration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Registration.setStatus("current")
_Mobile2Operator_Type = OctetString
_Mobile2Operator_Object = MibScalar
mobile2Operator = _Mobile2Operator_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 124),
    _Mobile2Operator_Type()
)
mobile2Operator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Operator.setStatus("current")
_Mobile2LAC_Type = OctetString
_Mobile2LAC_Object = MibScalar
mobile2LAC = _Mobile2LAC_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 125),
    _Mobile2LAC_Type()
)
mobile2LAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LAC.setStatus("current")
_Mobile2SignalQuality_Type = Integer32
_Mobile2SignalQuality_Object = MibScalar
mobile2SignalQuality = _Mobile2SignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 126),
    _Mobile2SignalQuality_Type()
)
mobile2SignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SignalQuality.setStatus("current")
_Mobile2CSQ_Type = Integer32
_Mobile2CSQ_Object = MibScalar
mobile2CSQ = _Mobile2CSQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 127),
    _Mobile2CSQ_Type()
)
mobile2CSQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2CSQ.setStatus("current")
_Mobile2PNOffset_Type = Integer32
_Mobile2PNOffset_Object = MibScalar
mobile2PNOffset = _Mobile2PNOffset_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 128),
    _Mobile2PNOffset_Type()
)
mobile2PNOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2PNOffset.setStatus("current")
_Mobile2Band_Type = OctetString
_Mobile2Band_Object = MibScalar
mobile2Band = _Mobile2Band_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 129),
    _Mobile2Band_Type()
)
mobile2Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2Band.setStatus("current")
_Mobile2RSSI_Type = Integer32
_Mobile2RSSI_Object = MibScalar
mobile2RSSI = _Mobile2RSSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 130),
    _Mobile2RSSI_Type()
)
mobile2RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2RSSI.setStatus("current")
_Mobile2RSCP_Type = Integer32
_Mobile2RSCP_Object = MibScalar
mobile2RSCP = _Mobile2RSCP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 131),
    _Mobile2RSCP_Type()
)
mobile2RSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2RSCP.setStatus("current")
_Mobile2RSRP_Type = Integer32
_Mobile2RSRP_Object = MibScalar
mobile2RSRP = _Mobile2RSRP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 132),
    _Mobile2RSRP_Type()
)
mobile2RSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2RSRP.setStatus("current")
_Mobile2RSRQ_Type = Integer32
_Mobile2RSRQ_Object = MibScalar
mobile2RSRQ = _Mobile2RSRQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 133),
    _Mobile2RSRQ_Type()
)
mobile2RSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2RSRQ.setStatus("current")
_Mobile2EcIo_Type = Integer32
_Mobile2EcIo_Object = MibScalar
mobile2EcIo = _Mobile2EcIo_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 134),
    _Mobile2EcIo_Type()
)
mobile2EcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2EcIo.setStatus("current")
_Mobile2NRBand_Type = OctetString
_Mobile2NRBand_Object = MibScalar
mobile2NRBand = _Mobile2NRBand_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 135),
    _Mobile2NRBand_Type()
)
mobile2NRBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRBand.setStatus("current")
_Mobile2NRChannel_Type = Integer32
_Mobile2NRChannel_Object = MibScalar
mobile2NRChannel = _Mobile2NRChannel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 136),
    _Mobile2NRChannel_Type()
)
mobile2NRChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRChannel.setStatus("current")
_Mobile2NRRSSI_Type = Integer32
_Mobile2NRRSSI_Object = MibScalar
mobile2NRRSSI = _Mobile2NRRSSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 137),
    _Mobile2NRRSSI_Type()
)
mobile2NRRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRRSSI.setStatus("current")
_Mobile2NRRSRP_Type = Integer32
_Mobile2NRRSRP_Object = MibScalar
mobile2NRRSRP = _Mobile2NRRSRP_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 138),
    _Mobile2NRRSRP_Type()
)
mobile2NRRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRRSRP.setStatus("current")
_Mobile2NRRSRQ_Type = Integer32
_Mobile2NRRSRQ_Object = MibScalar
mobile2NRRSRQ = _Mobile2NRRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 139),
    _Mobile2NRRSRQ_Type()
)
mobile2NRRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRRSRQ.setStatus("current")
_Mobile2NRSINR_Type = Integer32
_Mobile2NRSINR_Object = MibScalar
mobile2NRSINR = _Mobile2NRSINR_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 140),
    _Mobile2NRSINR_Type()
)
mobile2NRSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2NRSINR.setStatus("current")
_Mobile2SINR_Type = Integer32
_Mobile2SINR_Object = MibScalar
mobile2SINR = _Mobile2SINR_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 141),
    _Mobile2SINR_Type()
)
mobile2SINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2SINR.setStatus("current")
_Mobile_2_ObjectIdentity = ObjectIdentity
mobile_2 = _Mobile_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5)
)
_MobileToday_ObjectIdentity = ObjectIdentity
mobileToday = _MobileToday_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1)
)
_MobileTodayRxPri_Type = Counter32
_MobileTodayRxPri_Object = MibScalar
mobileTodayRxPri = _MobileTodayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 1),
    _MobileTodayRxPri_Type()
)
mobileTodayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayRxPri.setStatus("current")
_MobileTodayRxSec_Type = Counter32
_MobileTodayRxSec_Object = MibScalar
mobileTodayRxSec = _MobileTodayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 2),
    _MobileTodayRxSec_Type()
)
mobileTodayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayRxSec.setStatus("current")
_MobileTodayTxPri_Type = Counter32
_MobileTodayTxPri_Object = MibScalar
mobileTodayTxPri = _MobileTodayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 3),
    _MobileTodayTxPri_Type()
)
mobileTodayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayTxPri.setStatus("current")
_MobileTodayTxSec_Type = Counter32
_MobileTodayTxSec_Object = MibScalar
mobileTodayTxSec = _MobileTodayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 4),
    _MobileTodayTxSec_Type()
)
mobileTodayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayTxSec.setStatus("current")
_MobileTodayConnectionsPri_Type = Counter32
_MobileTodayConnectionsPri_Object = MibScalar
mobileTodayConnectionsPri = _MobileTodayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 5),
    _MobileTodayConnectionsPri_Type()
)
mobileTodayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayConnectionsPri.setStatus("current")
_MobileTodayConnectionsSec_Type = Counter32
_MobileTodayConnectionsSec_Object = MibScalar
mobileTodayConnectionsSec = _MobileTodayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 6),
    _MobileTodayConnectionsSec_Type()
)
mobileTodayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayConnectionsSec.setStatus("current")
_MobileTodayOnlinePri_Type = TimeTicks
_MobileTodayOnlinePri_Object = MibScalar
mobileTodayOnlinePri = _MobileTodayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 7),
    _MobileTodayOnlinePri_Type()
)
mobileTodayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayOnlinePri.setStatus("current")
_MobileTodayOnlineSec_Type = TimeTicks
_MobileTodayOnlineSec_Object = MibScalar
mobileTodayOnlineSec = _MobileTodayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 8),
    _MobileTodayOnlineSec_Type()
)
mobileTodayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayOnlineSec.setStatus("current")
_MobileTodayOffline_Type = TimeTicks
_MobileTodayOffline_Object = MibScalar
mobileTodayOffline = _MobileTodayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 9),
    _MobileTodayOffline_Type()
)
mobileTodayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayOffline.setStatus("current")
_MobileTodayCells_Type = Counter32
_MobileTodayCells_Object = MibScalar
mobileTodayCells = _MobileTodayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 10),
    _MobileTodayCells_Type()
)
mobileTodayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayCells.setStatus("current")
_MobileTodaySignalAvg_Type = Integer32
_MobileTodaySignalAvg_Object = MibScalar
mobileTodaySignalAvg = _MobileTodaySignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 11),
    _MobileTodaySignalAvg_Type()
)
mobileTodaySignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodaySignalAvg.setStatus("current")
_MobileTodaySignalMin_Type = Integer32
_MobileTodaySignalMin_Object = MibScalar
mobileTodaySignalMin = _MobileTodaySignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 12),
    _MobileTodaySignalMin_Type()
)
mobileTodaySignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodaySignalMin.setStatus("current")
_MobileTodaySignalMax_Type = Integer32
_MobileTodaySignalMax_Object = MibScalar
mobileTodaySignalMax = _MobileTodaySignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 13),
    _MobileTodaySignalMax_Type()
)
mobileTodaySignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodaySignalMax.setStatus("current")
_MobileTodayDateMin_Type = Counter32
_MobileTodayDateMin_Object = MibScalar
mobileTodayDateMin = _MobileTodayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 14),
    _MobileTodayDateMin_Type()
)
mobileTodayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayDateMin.setStatus("current")
_MobileTodayDateMax_Type = Counter32
_MobileTodayDateMax_Object = MibScalar
mobileTodayDateMax = _MobileTodayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 15),
    _MobileTodayDateMax_Type()
)
mobileTodayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileTodayDateMax.setStatus("current")
_Mobile2TodayRxPri_Type = Counter32
_Mobile2TodayRxPri_Object = MibScalar
mobile2TodayRxPri = _Mobile2TodayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 101),
    _Mobile2TodayRxPri_Type()
)
mobile2TodayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayRxPri.setStatus("current")
_Mobile2TodayRxSec_Type = Counter32
_Mobile2TodayRxSec_Object = MibScalar
mobile2TodayRxSec = _Mobile2TodayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 102),
    _Mobile2TodayRxSec_Type()
)
mobile2TodayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayRxSec.setStatus("current")
_Mobile2TodayTxPri_Type = Counter32
_Mobile2TodayTxPri_Object = MibScalar
mobile2TodayTxPri = _Mobile2TodayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 103),
    _Mobile2TodayTxPri_Type()
)
mobile2TodayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayTxPri.setStatus("current")
_Mobile2TodayTxSec_Type = Counter32
_Mobile2TodayTxSec_Object = MibScalar
mobile2TodayTxSec = _Mobile2TodayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 104),
    _Mobile2TodayTxSec_Type()
)
mobile2TodayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayTxSec.setStatus("current")
_Mobile2TodayConnectionsPri_Type = Counter32
_Mobile2TodayConnectionsPri_Object = MibScalar
mobile2TodayConnectionsPri = _Mobile2TodayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 105),
    _Mobile2TodayConnectionsPri_Type()
)
mobile2TodayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayConnectionsPri.setStatus("current")
_Mobile2TodayConnectionsSec_Type = Counter32
_Mobile2TodayConnectionsSec_Object = MibScalar
mobile2TodayConnectionsSec = _Mobile2TodayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 106),
    _Mobile2TodayConnectionsSec_Type()
)
mobile2TodayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayConnectionsSec.setStatus("current")
_Mobile2TodayOnlinePri_Type = TimeTicks
_Mobile2TodayOnlinePri_Object = MibScalar
mobile2TodayOnlinePri = _Mobile2TodayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 107),
    _Mobile2TodayOnlinePri_Type()
)
mobile2TodayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayOnlinePri.setStatus("current")
_Mobile2TodayOnlineSec_Type = TimeTicks
_Mobile2TodayOnlineSec_Object = MibScalar
mobile2TodayOnlineSec = _Mobile2TodayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 108),
    _Mobile2TodayOnlineSec_Type()
)
mobile2TodayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayOnlineSec.setStatus("current")
_Mobile2TodayOffline_Type = TimeTicks
_Mobile2TodayOffline_Object = MibScalar
mobile2TodayOffline = _Mobile2TodayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 109),
    _Mobile2TodayOffline_Type()
)
mobile2TodayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayOffline.setStatus("current")
_Mobile2TodayCells_Type = Counter32
_Mobile2TodayCells_Object = MibScalar
mobile2TodayCells = _Mobile2TodayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 110),
    _Mobile2TodayCells_Type()
)
mobile2TodayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayCells.setStatus("current")
_Mobile2TodaySignalAvg_Type = Integer32
_Mobile2TodaySignalAvg_Object = MibScalar
mobile2TodaySignalAvg = _Mobile2TodaySignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 111),
    _Mobile2TodaySignalAvg_Type()
)
mobile2TodaySignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodaySignalAvg.setStatus("current")
_Mobile2TodaySignalMin_Type = Integer32
_Mobile2TodaySignalMin_Object = MibScalar
mobile2TodaySignalMin = _Mobile2TodaySignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 112),
    _Mobile2TodaySignalMin_Type()
)
mobile2TodaySignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodaySignalMin.setStatus("current")
_Mobile2TodaySignalMax_Type = Integer32
_Mobile2TodaySignalMax_Object = MibScalar
mobile2TodaySignalMax = _Mobile2TodaySignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 113),
    _Mobile2TodaySignalMax_Type()
)
mobile2TodaySignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodaySignalMax.setStatus("current")
_Mobile2TodayDateMin_Type = Counter32
_Mobile2TodayDateMin_Object = MibScalar
mobile2TodayDateMin = _Mobile2TodayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 114),
    _Mobile2TodayDateMin_Type()
)
mobile2TodayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayDateMin.setStatus("current")
_Mobile2TodayDateMax_Type = Counter32
_Mobile2TodayDateMax_Object = MibScalar
mobile2TodayDateMax = _Mobile2TodayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 115),
    _Mobile2TodayDateMax_Type()
)
mobile2TodayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2TodayDateMax.setStatus("current")
_MobileYesterday_ObjectIdentity = ObjectIdentity
mobileYesterday = _MobileYesterday_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2)
)
_MobileYesterdayRxPri_Type = Counter32
_MobileYesterdayRxPri_Object = MibScalar
mobileYesterdayRxPri = _MobileYesterdayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 1),
    _MobileYesterdayRxPri_Type()
)
mobileYesterdayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayRxPri.setStatus("current")
_MobileYesterdayRxSec_Type = Counter32
_MobileYesterdayRxSec_Object = MibScalar
mobileYesterdayRxSec = _MobileYesterdayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 2),
    _MobileYesterdayRxSec_Type()
)
mobileYesterdayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayRxSec.setStatus("current")
_MobileYesterdayTxPri_Type = Counter32
_MobileYesterdayTxPri_Object = MibScalar
mobileYesterdayTxPri = _MobileYesterdayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 3),
    _MobileYesterdayTxPri_Type()
)
mobileYesterdayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayTxPri.setStatus("current")
_MobileYesterdayTxSec_Type = Counter32
_MobileYesterdayTxSec_Object = MibScalar
mobileYesterdayTxSec = _MobileYesterdayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 4),
    _MobileYesterdayTxSec_Type()
)
mobileYesterdayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayTxSec.setStatus("current")
_MobileYesterdayConnectionsPri_Type = Counter32
_MobileYesterdayConnectionsPri_Object = MibScalar
mobileYesterdayConnectionsPri = _MobileYesterdayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 5),
    _MobileYesterdayConnectionsPri_Type()
)
mobileYesterdayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayConnectionsPri.setStatus("current")
_MobileYesterdayConnectionsSec_Type = Counter32
_MobileYesterdayConnectionsSec_Object = MibScalar
mobileYesterdayConnectionsSec = _MobileYesterdayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 6),
    _MobileYesterdayConnectionsSec_Type()
)
mobileYesterdayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayConnectionsSec.setStatus("current")
_MobileYesterdayOnlinePri_Type = TimeTicks
_MobileYesterdayOnlinePri_Object = MibScalar
mobileYesterdayOnlinePri = _MobileYesterdayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 7),
    _MobileYesterdayOnlinePri_Type()
)
mobileYesterdayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayOnlinePri.setStatus("current")
_MobileYesterdayOnlineSec_Type = TimeTicks
_MobileYesterdayOnlineSec_Object = MibScalar
mobileYesterdayOnlineSec = _MobileYesterdayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 8),
    _MobileYesterdayOnlineSec_Type()
)
mobileYesterdayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayOnlineSec.setStatus("current")
_MobileYesterdayOffline_Type = TimeTicks
_MobileYesterdayOffline_Object = MibScalar
mobileYesterdayOffline = _MobileYesterdayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 9),
    _MobileYesterdayOffline_Type()
)
mobileYesterdayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayOffline.setStatus("current")
_MobileYesterdayCells_Type = Counter32
_MobileYesterdayCells_Object = MibScalar
mobileYesterdayCells = _MobileYesterdayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 10),
    _MobileYesterdayCells_Type()
)
mobileYesterdayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayCells.setStatus("current")
_MobileYesterdaySignalAvg_Type = Integer32
_MobileYesterdaySignalAvg_Object = MibScalar
mobileYesterdaySignalAvg = _MobileYesterdaySignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 11),
    _MobileYesterdaySignalAvg_Type()
)
mobileYesterdaySignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdaySignalAvg.setStatus("current")
_MobileYesterdaySignalMin_Type = Integer32
_MobileYesterdaySignalMin_Object = MibScalar
mobileYesterdaySignalMin = _MobileYesterdaySignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 12),
    _MobileYesterdaySignalMin_Type()
)
mobileYesterdaySignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdaySignalMin.setStatus("current")
_MobileYesterdaySignalMax_Type = Integer32
_MobileYesterdaySignalMax_Object = MibScalar
mobileYesterdaySignalMax = _MobileYesterdaySignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 13),
    _MobileYesterdaySignalMax_Type()
)
mobileYesterdaySignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdaySignalMax.setStatus("current")
_MobileYesterdayDateMin_Type = Counter32
_MobileYesterdayDateMin_Object = MibScalar
mobileYesterdayDateMin = _MobileYesterdayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 14),
    _MobileYesterdayDateMin_Type()
)
mobileYesterdayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayDateMin.setStatus("current")
_MobileYesterdayDateMax_Type = Counter32
_MobileYesterdayDateMax_Object = MibScalar
mobileYesterdayDateMax = _MobileYesterdayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 15),
    _MobileYesterdayDateMax_Type()
)
mobileYesterdayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileYesterdayDateMax.setStatus("current")
_Mobile2YesterdayRxPri_Type = Counter32
_Mobile2YesterdayRxPri_Object = MibScalar
mobile2YesterdayRxPri = _Mobile2YesterdayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 101),
    _Mobile2YesterdayRxPri_Type()
)
mobile2YesterdayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayRxPri.setStatus("current")
_Mobile2YesterdayRxSec_Type = Counter32
_Mobile2YesterdayRxSec_Object = MibScalar
mobile2YesterdayRxSec = _Mobile2YesterdayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 102),
    _Mobile2YesterdayRxSec_Type()
)
mobile2YesterdayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayRxSec.setStatus("current")
_Mobile2YesterdayTxPri_Type = Counter32
_Mobile2YesterdayTxPri_Object = MibScalar
mobile2YesterdayTxPri = _Mobile2YesterdayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 103),
    _Mobile2YesterdayTxPri_Type()
)
mobile2YesterdayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayTxPri.setStatus("current")
_Mobile2YesterdayTxSec_Type = Counter32
_Mobile2YesterdayTxSec_Object = MibScalar
mobile2YesterdayTxSec = _Mobile2YesterdayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 104),
    _Mobile2YesterdayTxSec_Type()
)
mobile2YesterdayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayTxSec.setStatus("current")
_Mobile2YesterdayConnectionsPri_Type = Counter32
_Mobile2YesterdayConnectionsPri_Object = MibScalar
mobile2YesterdayConnectionsPri = _Mobile2YesterdayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 105),
    _Mobile2YesterdayConnectionsPri_Type()
)
mobile2YesterdayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayConnectionsPri.setStatus("current")
_Mobile2YesterdayConnectionsSec_Type = Counter32
_Mobile2YesterdayConnectionsSec_Object = MibScalar
mobile2YesterdayConnectionsSec = _Mobile2YesterdayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 106),
    _Mobile2YesterdayConnectionsSec_Type()
)
mobile2YesterdayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayConnectionsSec.setStatus("current")
_Mobile2YesterdayOnlinePri_Type = TimeTicks
_Mobile2YesterdayOnlinePri_Object = MibScalar
mobile2YesterdayOnlinePri = _Mobile2YesterdayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 107),
    _Mobile2YesterdayOnlinePri_Type()
)
mobile2YesterdayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayOnlinePri.setStatus("current")
_Mobile2YesterdayOnlineSec_Type = TimeTicks
_Mobile2YesterdayOnlineSec_Object = MibScalar
mobile2YesterdayOnlineSec = _Mobile2YesterdayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 108),
    _Mobile2YesterdayOnlineSec_Type()
)
mobile2YesterdayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayOnlineSec.setStatus("current")
_Mobile2YesterdayOffline_Type = TimeTicks
_Mobile2YesterdayOffline_Object = MibScalar
mobile2YesterdayOffline = _Mobile2YesterdayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 109),
    _Mobile2YesterdayOffline_Type()
)
mobile2YesterdayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayOffline.setStatus("current")
_Mobile2YesterdayCells_Type = Counter32
_Mobile2YesterdayCells_Object = MibScalar
mobile2YesterdayCells = _Mobile2YesterdayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 110),
    _Mobile2YesterdayCells_Type()
)
mobile2YesterdayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayCells.setStatus("current")
_Mobile2YesterdaySignalAvg_Type = Integer32
_Mobile2YesterdaySignalAvg_Object = MibScalar
mobile2YesterdaySignalAvg = _Mobile2YesterdaySignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 111),
    _Mobile2YesterdaySignalAvg_Type()
)
mobile2YesterdaySignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdaySignalAvg.setStatus("current")
_Mobile2YesterdaySignalMin_Type = Integer32
_Mobile2YesterdaySignalMin_Object = MibScalar
mobile2YesterdaySignalMin = _Mobile2YesterdaySignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 112),
    _Mobile2YesterdaySignalMin_Type()
)
mobile2YesterdaySignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdaySignalMin.setStatus("current")
_Mobile2YesterdaySignalMax_Type = Integer32
_Mobile2YesterdaySignalMax_Object = MibScalar
mobile2YesterdaySignalMax = _Mobile2YesterdaySignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 113),
    _Mobile2YesterdaySignalMax_Type()
)
mobile2YesterdaySignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdaySignalMax.setStatus("current")
_Mobile2YesterdayDateMin_Type = Counter32
_Mobile2YesterdayDateMin_Object = MibScalar
mobile2YesterdayDateMin = _Mobile2YesterdayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 114),
    _Mobile2YesterdayDateMin_Type()
)
mobile2YesterdayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayDateMin.setStatus("current")
_Mobile2YesterdayDateMax_Type = Counter32
_Mobile2YesterdayDateMax_Object = MibScalar
mobile2YesterdayDateMax = _Mobile2YesterdayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 115),
    _Mobile2YesterdayDateMax_Type()
)
mobile2YesterdayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2YesterdayDateMax.setStatus("current")
_MobileThisWeek_ObjectIdentity = ObjectIdentity
mobileThisWeek = _MobileThisWeek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3)
)
_MobileThisWeekRxPri_Type = Counter32
_MobileThisWeekRxPri_Object = MibScalar
mobileThisWeekRxPri = _MobileThisWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 1),
    _MobileThisWeekRxPri_Type()
)
mobileThisWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekRxPri.setStatus("current")
_MobileThisWeekRxSec_Type = Counter32
_MobileThisWeekRxSec_Object = MibScalar
mobileThisWeekRxSec = _MobileThisWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 2),
    _MobileThisWeekRxSec_Type()
)
mobileThisWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekRxSec.setStatus("current")
_MobileThisWeekTxPri_Type = Counter32
_MobileThisWeekTxPri_Object = MibScalar
mobileThisWeekTxPri = _MobileThisWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 3),
    _MobileThisWeekTxPri_Type()
)
mobileThisWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekTxPri.setStatus("current")
_MobileThisWeekTxSec_Type = Counter32
_MobileThisWeekTxSec_Object = MibScalar
mobileThisWeekTxSec = _MobileThisWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 4),
    _MobileThisWeekTxSec_Type()
)
mobileThisWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekTxSec.setStatus("current")
_MobileThisWeekConnectionsPri_Type = Counter32
_MobileThisWeekConnectionsPri_Object = MibScalar
mobileThisWeekConnectionsPri = _MobileThisWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 5),
    _MobileThisWeekConnectionsPri_Type()
)
mobileThisWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekConnectionsPri.setStatus("current")
_MobileThisWeekConnectionsSec_Type = Counter32
_MobileThisWeekConnectionsSec_Object = MibScalar
mobileThisWeekConnectionsSec = _MobileThisWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 6),
    _MobileThisWeekConnectionsSec_Type()
)
mobileThisWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekConnectionsSec.setStatus("current")
_MobileThisWeekOnlinePri_Type = TimeTicks
_MobileThisWeekOnlinePri_Object = MibScalar
mobileThisWeekOnlinePri = _MobileThisWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 7),
    _MobileThisWeekOnlinePri_Type()
)
mobileThisWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekOnlinePri.setStatus("current")
_MobileThisWeekOnlineSec_Type = TimeTicks
_MobileThisWeekOnlineSec_Object = MibScalar
mobileThisWeekOnlineSec = _MobileThisWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 8),
    _MobileThisWeekOnlineSec_Type()
)
mobileThisWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekOnlineSec.setStatus("current")
_MobileThisWeekOffline_Type = TimeTicks
_MobileThisWeekOffline_Object = MibScalar
mobileThisWeekOffline = _MobileThisWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 9),
    _MobileThisWeekOffline_Type()
)
mobileThisWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekOffline.setStatus("current")
_MobileThisWeekCells_Type = Counter32
_MobileThisWeekCells_Object = MibScalar
mobileThisWeekCells = _MobileThisWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 10),
    _MobileThisWeekCells_Type()
)
mobileThisWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekCells.setStatus("current")
_MobileThisWeekSignalAvg_Type = Integer32
_MobileThisWeekSignalAvg_Object = MibScalar
mobileThisWeekSignalAvg = _MobileThisWeekSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 11),
    _MobileThisWeekSignalAvg_Type()
)
mobileThisWeekSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekSignalAvg.setStatus("current")
_MobileThisWeekSignalMin_Type = Integer32
_MobileThisWeekSignalMin_Object = MibScalar
mobileThisWeekSignalMin = _MobileThisWeekSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 12),
    _MobileThisWeekSignalMin_Type()
)
mobileThisWeekSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekSignalMin.setStatus("current")
_MobileThisWeekSignalMax_Type = Integer32
_MobileThisWeekSignalMax_Object = MibScalar
mobileThisWeekSignalMax = _MobileThisWeekSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 13),
    _MobileThisWeekSignalMax_Type()
)
mobileThisWeekSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekSignalMax.setStatus("current")
_MobileThisWeekDateMin_Type = Counter32
_MobileThisWeekDateMin_Object = MibScalar
mobileThisWeekDateMin = _MobileThisWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 14),
    _MobileThisWeekDateMin_Type()
)
mobileThisWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekDateMin.setStatus("current")
_MobileThisWeekDateMax_Type = Counter32
_MobileThisWeekDateMax_Object = MibScalar
mobileThisWeekDateMax = _MobileThisWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 15),
    _MobileThisWeekDateMax_Type()
)
mobileThisWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisWeekDateMax.setStatus("current")
_Mobile2ThisWeekRxPri_Type = Counter32
_Mobile2ThisWeekRxPri_Object = MibScalar
mobile2ThisWeekRxPri = _Mobile2ThisWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 101),
    _Mobile2ThisWeekRxPri_Type()
)
mobile2ThisWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekRxPri.setStatus("current")
_Mobile2ThisWeekRxSec_Type = Counter32
_Mobile2ThisWeekRxSec_Object = MibScalar
mobile2ThisWeekRxSec = _Mobile2ThisWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 102),
    _Mobile2ThisWeekRxSec_Type()
)
mobile2ThisWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekRxSec.setStatus("current")
_Mobile2ThisWeekTxPri_Type = Counter32
_Mobile2ThisWeekTxPri_Object = MibScalar
mobile2ThisWeekTxPri = _Mobile2ThisWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 103),
    _Mobile2ThisWeekTxPri_Type()
)
mobile2ThisWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekTxPri.setStatus("current")
_Mobile2ThisWeekTxSec_Type = Counter32
_Mobile2ThisWeekTxSec_Object = MibScalar
mobile2ThisWeekTxSec = _Mobile2ThisWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 104),
    _Mobile2ThisWeekTxSec_Type()
)
mobile2ThisWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekTxSec.setStatus("current")
_Mobile2ThisWeekConnectionsPri_Type = Counter32
_Mobile2ThisWeekConnectionsPri_Object = MibScalar
mobile2ThisWeekConnectionsPri = _Mobile2ThisWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 105),
    _Mobile2ThisWeekConnectionsPri_Type()
)
mobile2ThisWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekConnectionsPri.setStatus("current")
_Mobile2ThisWeekConnectionsSec_Type = Counter32
_Mobile2ThisWeekConnectionsSec_Object = MibScalar
mobile2ThisWeekConnectionsSec = _Mobile2ThisWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 106),
    _Mobile2ThisWeekConnectionsSec_Type()
)
mobile2ThisWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekConnectionsSec.setStatus("current")
_Mobile2ThisWeekOnlinePri_Type = TimeTicks
_Mobile2ThisWeekOnlinePri_Object = MibScalar
mobile2ThisWeekOnlinePri = _Mobile2ThisWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 107),
    _Mobile2ThisWeekOnlinePri_Type()
)
mobile2ThisWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekOnlinePri.setStatus("current")
_Mobile2ThisWeekOnlineSec_Type = TimeTicks
_Mobile2ThisWeekOnlineSec_Object = MibScalar
mobile2ThisWeekOnlineSec = _Mobile2ThisWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 108),
    _Mobile2ThisWeekOnlineSec_Type()
)
mobile2ThisWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekOnlineSec.setStatus("current")
_Mobile2ThisWeekOffline_Type = TimeTicks
_Mobile2ThisWeekOffline_Object = MibScalar
mobile2ThisWeekOffline = _Mobile2ThisWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 109),
    _Mobile2ThisWeekOffline_Type()
)
mobile2ThisWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekOffline.setStatus("current")
_Mobile2ThisWeekCells_Type = Counter32
_Mobile2ThisWeekCells_Object = MibScalar
mobile2ThisWeekCells = _Mobile2ThisWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 110),
    _Mobile2ThisWeekCells_Type()
)
mobile2ThisWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekCells.setStatus("current")
_Mobile2ThisWeekSignalAvg_Type = Integer32
_Mobile2ThisWeekSignalAvg_Object = MibScalar
mobile2ThisWeekSignalAvg = _Mobile2ThisWeekSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 111),
    _Mobile2ThisWeekSignalAvg_Type()
)
mobile2ThisWeekSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekSignalAvg.setStatus("current")
_Mobile2ThisWeekSignalMin_Type = Integer32
_Mobile2ThisWeekSignalMin_Object = MibScalar
mobile2ThisWeekSignalMin = _Mobile2ThisWeekSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 112),
    _Mobile2ThisWeekSignalMin_Type()
)
mobile2ThisWeekSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekSignalMin.setStatus("current")
_Mobile2ThisWeekSignalMax_Type = Integer32
_Mobile2ThisWeekSignalMax_Object = MibScalar
mobile2ThisWeekSignalMax = _Mobile2ThisWeekSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 113),
    _Mobile2ThisWeekSignalMax_Type()
)
mobile2ThisWeekSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekSignalMax.setStatus("current")
_Mobile2ThisWeekDateMin_Type = Counter32
_Mobile2ThisWeekDateMin_Object = MibScalar
mobile2ThisWeekDateMin = _Mobile2ThisWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 114),
    _Mobile2ThisWeekDateMin_Type()
)
mobile2ThisWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekDateMin.setStatus("current")
_Mobile2ThisWeekDateMax_Type = Counter32
_Mobile2ThisWeekDateMax_Object = MibScalar
mobile2ThisWeekDateMax = _Mobile2ThisWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 115),
    _Mobile2ThisWeekDateMax_Type()
)
mobile2ThisWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisWeekDateMax.setStatus("current")
_MobileLastWeek_ObjectIdentity = ObjectIdentity
mobileLastWeek = _MobileLastWeek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4)
)
_MobileLastWeekRxPri_Type = Counter32
_MobileLastWeekRxPri_Object = MibScalar
mobileLastWeekRxPri = _MobileLastWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 1),
    _MobileLastWeekRxPri_Type()
)
mobileLastWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekRxPri.setStatus("current")
_MobileLastWeekRxSec_Type = Counter32
_MobileLastWeekRxSec_Object = MibScalar
mobileLastWeekRxSec = _MobileLastWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 2),
    _MobileLastWeekRxSec_Type()
)
mobileLastWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekRxSec.setStatus("current")
_MobileLastWeekTxPri_Type = Counter32
_MobileLastWeekTxPri_Object = MibScalar
mobileLastWeekTxPri = _MobileLastWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 3),
    _MobileLastWeekTxPri_Type()
)
mobileLastWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekTxPri.setStatus("current")
_MobileLastWeekTxSec_Type = Counter32
_MobileLastWeekTxSec_Object = MibScalar
mobileLastWeekTxSec = _MobileLastWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 4),
    _MobileLastWeekTxSec_Type()
)
mobileLastWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekTxSec.setStatus("current")
_MobileLastWeekConnectionsPri_Type = Counter32
_MobileLastWeekConnectionsPri_Object = MibScalar
mobileLastWeekConnectionsPri = _MobileLastWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 5),
    _MobileLastWeekConnectionsPri_Type()
)
mobileLastWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekConnectionsPri.setStatus("current")
_MobileLastWeekConnectionsSec_Type = Counter32
_MobileLastWeekConnectionsSec_Object = MibScalar
mobileLastWeekConnectionsSec = _MobileLastWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 6),
    _MobileLastWeekConnectionsSec_Type()
)
mobileLastWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekConnectionsSec.setStatus("current")
_MobileLastWeekOnlinePri_Type = TimeTicks
_MobileLastWeekOnlinePri_Object = MibScalar
mobileLastWeekOnlinePri = _MobileLastWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 7),
    _MobileLastWeekOnlinePri_Type()
)
mobileLastWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekOnlinePri.setStatus("current")
_MobileLastWeekOnlineSec_Type = TimeTicks
_MobileLastWeekOnlineSec_Object = MibScalar
mobileLastWeekOnlineSec = _MobileLastWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 8),
    _MobileLastWeekOnlineSec_Type()
)
mobileLastWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekOnlineSec.setStatus("current")
_MobileLastWeekOffline_Type = TimeTicks
_MobileLastWeekOffline_Object = MibScalar
mobileLastWeekOffline = _MobileLastWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 9),
    _MobileLastWeekOffline_Type()
)
mobileLastWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekOffline.setStatus("current")
_MobileLastWeekCells_Type = Counter32
_MobileLastWeekCells_Object = MibScalar
mobileLastWeekCells = _MobileLastWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 10),
    _MobileLastWeekCells_Type()
)
mobileLastWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekCells.setStatus("current")
_MobileLastWeekSignalAvg_Type = Integer32
_MobileLastWeekSignalAvg_Object = MibScalar
mobileLastWeekSignalAvg = _MobileLastWeekSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 11),
    _MobileLastWeekSignalAvg_Type()
)
mobileLastWeekSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekSignalAvg.setStatus("current")
_MobileLastWeekSignalMin_Type = Integer32
_MobileLastWeekSignalMin_Object = MibScalar
mobileLastWeekSignalMin = _MobileLastWeekSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 12),
    _MobileLastWeekSignalMin_Type()
)
mobileLastWeekSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekSignalMin.setStatus("current")
_MobileLastWeekSignalMax_Type = Integer32
_MobileLastWeekSignalMax_Object = MibScalar
mobileLastWeekSignalMax = _MobileLastWeekSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 13),
    _MobileLastWeekSignalMax_Type()
)
mobileLastWeekSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekSignalMax.setStatus("current")
_MobileLastWeekDateMin_Type = Counter32
_MobileLastWeekDateMin_Object = MibScalar
mobileLastWeekDateMin = _MobileLastWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 14),
    _MobileLastWeekDateMin_Type()
)
mobileLastWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekDateMin.setStatus("current")
_MobileLastWeekDateMax_Type = Counter32
_MobileLastWeekDateMax_Object = MibScalar
mobileLastWeekDateMax = _MobileLastWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 15),
    _MobileLastWeekDateMax_Type()
)
mobileLastWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastWeekDateMax.setStatus("current")
_Mobile2LastWeekRxPri_Type = Counter32
_Mobile2LastWeekRxPri_Object = MibScalar
mobile2LastWeekRxPri = _Mobile2LastWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 101),
    _Mobile2LastWeekRxPri_Type()
)
mobile2LastWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekRxPri.setStatus("current")
_Mobile2LastWeekRxSec_Type = Counter32
_Mobile2LastWeekRxSec_Object = MibScalar
mobile2LastWeekRxSec = _Mobile2LastWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 102),
    _Mobile2LastWeekRxSec_Type()
)
mobile2LastWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekRxSec.setStatus("current")
_Mobile2LastWeekTxPri_Type = Counter32
_Mobile2LastWeekTxPri_Object = MibScalar
mobile2LastWeekTxPri = _Mobile2LastWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 103),
    _Mobile2LastWeekTxPri_Type()
)
mobile2LastWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekTxPri.setStatus("current")
_Mobile2LastWeekTxSec_Type = Counter32
_Mobile2LastWeekTxSec_Object = MibScalar
mobile2LastWeekTxSec = _Mobile2LastWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 104),
    _Mobile2LastWeekTxSec_Type()
)
mobile2LastWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekTxSec.setStatus("current")
_Mobile2LastWeekConnectionsPri_Type = Counter32
_Mobile2LastWeekConnectionsPri_Object = MibScalar
mobile2LastWeekConnectionsPri = _Mobile2LastWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 105),
    _Mobile2LastWeekConnectionsPri_Type()
)
mobile2LastWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekConnectionsPri.setStatus("current")
_Mobile2LastWeekConnectionsSec_Type = Counter32
_Mobile2LastWeekConnectionsSec_Object = MibScalar
mobile2LastWeekConnectionsSec = _Mobile2LastWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 106),
    _Mobile2LastWeekConnectionsSec_Type()
)
mobile2LastWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekConnectionsSec.setStatus("current")
_Mobile2LastWeekOnlinePri_Type = TimeTicks
_Mobile2LastWeekOnlinePri_Object = MibScalar
mobile2LastWeekOnlinePri = _Mobile2LastWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 107),
    _Mobile2LastWeekOnlinePri_Type()
)
mobile2LastWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekOnlinePri.setStatus("current")
_Mobile2LastWeekOnlineSec_Type = TimeTicks
_Mobile2LastWeekOnlineSec_Object = MibScalar
mobile2LastWeekOnlineSec = _Mobile2LastWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 108),
    _Mobile2LastWeekOnlineSec_Type()
)
mobile2LastWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekOnlineSec.setStatus("current")
_Mobile2LastWeekOffline_Type = TimeTicks
_Mobile2LastWeekOffline_Object = MibScalar
mobile2LastWeekOffline = _Mobile2LastWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 109),
    _Mobile2LastWeekOffline_Type()
)
mobile2LastWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekOffline.setStatus("current")
_Mobile2LastWeekCells_Type = Counter32
_Mobile2LastWeekCells_Object = MibScalar
mobile2LastWeekCells = _Mobile2LastWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 110),
    _Mobile2LastWeekCells_Type()
)
mobile2LastWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekCells.setStatus("current")
_Mobile2LastWeekSignalAvg_Type = Integer32
_Mobile2LastWeekSignalAvg_Object = MibScalar
mobile2LastWeekSignalAvg = _Mobile2LastWeekSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 111),
    _Mobile2LastWeekSignalAvg_Type()
)
mobile2LastWeekSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekSignalAvg.setStatus("current")
_Mobile2LastWeekSignalMin_Type = Integer32
_Mobile2LastWeekSignalMin_Object = MibScalar
mobile2LastWeekSignalMin = _Mobile2LastWeekSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 112),
    _Mobile2LastWeekSignalMin_Type()
)
mobile2LastWeekSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekSignalMin.setStatus("current")
_Mobile2LastWeekSignalMax_Type = Integer32
_Mobile2LastWeekSignalMax_Object = MibScalar
mobile2LastWeekSignalMax = _Mobile2LastWeekSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 113),
    _Mobile2LastWeekSignalMax_Type()
)
mobile2LastWeekSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekSignalMax.setStatus("current")
_Mobile2LastWeekDateMin_Type = Counter32
_Mobile2LastWeekDateMin_Object = MibScalar
mobile2LastWeekDateMin = _Mobile2LastWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 114),
    _Mobile2LastWeekDateMin_Type()
)
mobile2LastWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekDateMin.setStatus("current")
_Mobile2LastWeekDateMax_Type = Counter32
_Mobile2LastWeekDateMax_Object = MibScalar
mobile2LastWeekDateMax = _Mobile2LastWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 115),
    _Mobile2LastWeekDateMax_Type()
)
mobile2LastWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastWeekDateMax.setStatus("current")
_MobileThisPeriod_ObjectIdentity = ObjectIdentity
mobileThisPeriod = _MobileThisPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5)
)
_MobileThisPeriodRxPri_Type = Counter32
_MobileThisPeriodRxPri_Object = MibScalar
mobileThisPeriodRxPri = _MobileThisPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 1),
    _MobileThisPeriodRxPri_Type()
)
mobileThisPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodRxPri.setStatus("current")
_MobileThisPeriodRxSec_Type = Counter32
_MobileThisPeriodRxSec_Object = MibScalar
mobileThisPeriodRxSec = _MobileThisPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 2),
    _MobileThisPeriodRxSec_Type()
)
mobileThisPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodRxSec.setStatus("current")
_MobileThisPeriodTxPri_Type = Counter32
_MobileThisPeriodTxPri_Object = MibScalar
mobileThisPeriodTxPri = _MobileThisPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 3),
    _MobileThisPeriodTxPri_Type()
)
mobileThisPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodTxPri.setStatus("current")
_MobileThisPeriodTxSec_Type = Counter32
_MobileThisPeriodTxSec_Object = MibScalar
mobileThisPeriodTxSec = _MobileThisPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 4),
    _MobileThisPeriodTxSec_Type()
)
mobileThisPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodTxSec.setStatus("current")
_MobileThisPeriodConnectionsPri_Type = Counter32
_MobileThisPeriodConnectionsPri_Object = MibScalar
mobileThisPeriodConnectionsPri = _MobileThisPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 5),
    _MobileThisPeriodConnectionsPri_Type()
)
mobileThisPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodConnectionsPri.setStatus("current")
_MobileThisPeriodConnectionsSec_Type = Counter32
_MobileThisPeriodConnectionsSec_Object = MibScalar
mobileThisPeriodConnectionsSec = _MobileThisPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 6),
    _MobileThisPeriodConnectionsSec_Type()
)
mobileThisPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodConnectionsSec.setStatus("current")
_MobileThisPeriodOnlinePri_Type = TimeTicks
_MobileThisPeriodOnlinePri_Object = MibScalar
mobileThisPeriodOnlinePri = _MobileThisPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 7),
    _MobileThisPeriodOnlinePri_Type()
)
mobileThisPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodOnlinePri.setStatus("current")
_MobileThisPeriodOnlineSec_Type = TimeTicks
_MobileThisPeriodOnlineSec_Object = MibScalar
mobileThisPeriodOnlineSec = _MobileThisPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 8),
    _MobileThisPeriodOnlineSec_Type()
)
mobileThisPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodOnlineSec.setStatus("current")
_MobileThisPeriodOffline_Type = TimeTicks
_MobileThisPeriodOffline_Object = MibScalar
mobileThisPeriodOffline = _MobileThisPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 9),
    _MobileThisPeriodOffline_Type()
)
mobileThisPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodOffline.setStatus("current")
_MobileThisPeriodCells_Type = Counter32
_MobileThisPeriodCells_Object = MibScalar
mobileThisPeriodCells = _MobileThisPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 10),
    _MobileThisPeriodCells_Type()
)
mobileThisPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodCells.setStatus("current")
_MobileThisPeriodSignalAvg_Type = Integer32
_MobileThisPeriodSignalAvg_Object = MibScalar
mobileThisPeriodSignalAvg = _MobileThisPeriodSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 11),
    _MobileThisPeriodSignalAvg_Type()
)
mobileThisPeriodSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodSignalAvg.setStatus("current")
_MobileThisPeriodSignalMin_Type = Integer32
_MobileThisPeriodSignalMin_Object = MibScalar
mobileThisPeriodSignalMin = _MobileThisPeriodSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 12),
    _MobileThisPeriodSignalMin_Type()
)
mobileThisPeriodSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodSignalMin.setStatus("current")
_MobileThisPeriodSignalMax_Type = Integer32
_MobileThisPeriodSignalMax_Object = MibScalar
mobileThisPeriodSignalMax = _MobileThisPeriodSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 13),
    _MobileThisPeriodSignalMax_Type()
)
mobileThisPeriodSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodSignalMax.setStatus("current")
_MobileThisPeriodDateMin_Type = Counter32
_MobileThisPeriodDateMin_Object = MibScalar
mobileThisPeriodDateMin = _MobileThisPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 14),
    _MobileThisPeriodDateMin_Type()
)
mobileThisPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodDateMin.setStatus("current")
_MobileThisPeriodDateMax_Type = Counter32
_MobileThisPeriodDateMax_Object = MibScalar
mobileThisPeriodDateMax = _MobileThisPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 15),
    _MobileThisPeriodDateMax_Type()
)
mobileThisPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileThisPeriodDateMax.setStatus("current")
_Mobile2ThisPeriodRxPri_Type = Counter32
_Mobile2ThisPeriodRxPri_Object = MibScalar
mobile2ThisPeriodRxPri = _Mobile2ThisPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 101),
    _Mobile2ThisPeriodRxPri_Type()
)
mobile2ThisPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodRxPri.setStatus("current")
_Mobile2ThisPeriodRxSec_Type = Counter32
_Mobile2ThisPeriodRxSec_Object = MibScalar
mobile2ThisPeriodRxSec = _Mobile2ThisPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 102),
    _Mobile2ThisPeriodRxSec_Type()
)
mobile2ThisPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodRxSec.setStatus("current")
_Mobile2ThisPeriodTxPri_Type = Counter32
_Mobile2ThisPeriodTxPri_Object = MibScalar
mobile2ThisPeriodTxPri = _Mobile2ThisPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 103),
    _Mobile2ThisPeriodTxPri_Type()
)
mobile2ThisPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodTxPri.setStatus("current")
_Mobile2ThisPeriodTxSec_Type = Counter32
_Mobile2ThisPeriodTxSec_Object = MibScalar
mobile2ThisPeriodTxSec = _Mobile2ThisPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 104),
    _Mobile2ThisPeriodTxSec_Type()
)
mobile2ThisPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodTxSec.setStatus("current")
_Mobile2ThisPeriodConnectionsPri_Type = Counter32
_Mobile2ThisPeriodConnectionsPri_Object = MibScalar
mobile2ThisPeriodConnectionsPri = _Mobile2ThisPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 105),
    _Mobile2ThisPeriodConnectionsPri_Type()
)
mobile2ThisPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodConnectionsPri.setStatus("current")
_Mobile2ThisPeriodConnectionsSec_Type = Counter32
_Mobile2ThisPeriodConnectionsSec_Object = MibScalar
mobile2ThisPeriodConnectionsSec = _Mobile2ThisPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 106),
    _Mobile2ThisPeriodConnectionsSec_Type()
)
mobile2ThisPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodConnectionsSec.setStatus("current")
_Mobile2ThisPeriodOnlinePri_Type = TimeTicks
_Mobile2ThisPeriodOnlinePri_Object = MibScalar
mobile2ThisPeriodOnlinePri = _Mobile2ThisPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 107),
    _Mobile2ThisPeriodOnlinePri_Type()
)
mobile2ThisPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodOnlinePri.setStatus("current")
_Mobile2ThisPeriodOnlineSec_Type = TimeTicks
_Mobile2ThisPeriodOnlineSec_Object = MibScalar
mobile2ThisPeriodOnlineSec = _Mobile2ThisPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 108),
    _Mobile2ThisPeriodOnlineSec_Type()
)
mobile2ThisPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodOnlineSec.setStatus("current")
_Mobile2ThisPeriodOffline_Type = TimeTicks
_Mobile2ThisPeriodOffline_Object = MibScalar
mobile2ThisPeriodOffline = _Mobile2ThisPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 109),
    _Mobile2ThisPeriodOffline_Type()
)
mobile2ThisPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodOffline.setStatus("current")
_Mobile2ThisPeriodCells_Type = Counter32
_Mobile2ThisPeriodCells_Object = MibScalar
mobile2ThisPeriodCells = _Mobile2ThisPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 110),
    _Mobile2ThisPeriodCells_Type()
)
mobile2ThisPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodCells.setStatus("current")
_Mobile2ThisPeriodSignalAvg_Type = Integer32
_Mobile2ThisPeriodSignalAvg_Object = MibScalar
mobile2ThisPeriodSignalAvg = _Mobile2ThisPeriodSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 111),
    _Mobile2ThisPeriodSignalAvg_Type()
)
mobile2ThisPeriodSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodSignalAvg.setStatus("current")
_Mobile2ThisPeriodSignalMin_Type = Integer32
_Mobile2ThisPeriodSignalMin_Object = MibScalar
mobile2ThisPeriodSignalMin = _Mobile2ThisPeriodSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 112),
    _Mobile2ThisPeriodSignalMin_Type()
)
mobile2ThisPeriodSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodSignalMin.setStatus("current")
_Mobile2ThisPeriodSignalMax_Type = Integer32
_Mobile2ThisPeriodSignalMax_Object = MibScalar
mobile2ThisPeriodSignalMax = _Mobile2ThisPeriodSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 113),
    _Mobile2ThisPeriodSignalMax_Type()
)
mobile2ThisPeriodSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodSignalMax.setStatus("current")
_Mobile2ThisPeriodDateMin_Type = Counter32
_Mobile2ThisPeriodDateMin_Object = MibScalar
mobile2ThisPeriodDateMin = _Mobile2ThisPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 114),
    _Mobile2ThisPeriodDateMin_Type()
)
mobile2ThisPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodDateMin.setStatus("current")
_Mobile2ThisPeriodDateMax_Type = Counter32
_Mobile2ThisPeriodDateMax_Object = MibScalar
mobile2ThisPeriodDateMax = _Mobile2ThisPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 115),
    _Mobile2ThisPeriodDateMax_Type()
)
mobile2ThisPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2ThisPeriodDateMax.setStatus("current")
_MobileLastPeriod_ObjectIdentity = ObjectIdentity
mobileLastPeriod = _MobileLastPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6)
)
_MobileLastPeriodRxPri_Type = Counter32
_MobileLastPeriodRxPri_Object = MibScalar
mobileLastPeriodRxPri = _MobileLastPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 1),
    _MobileLastPeriodRxPri_Type()
)
mobileLastPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodRxPri.setStatus("current")
_MobileLastPeriodRxSec_Type = Counter32
_MobileLastPeriodRxSec_Object = MibScalar
mobileLastPeriodRxSec = _MobileLastPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 2),
    _MobileLastPeriodRxSec_Type()
)
mobileLastPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodRxSec.setStatus("current")
_MobileLastPeriodTxPri_Type = Counter32
_MobileLastPeriodTxPri_Object = MibScalar
mobileLastPeriodTxPri = _MobileLastPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 3),
    _MobileLastPeriodTxPri_Type()
)
mobileLastPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodTxPri.setStatus("current")
_MobileLastPeriodTxSec_Type = Counter32
_MobileLastPeriodTxSec_Object = MibScalar
mobileLastPeriodTxSec = _MobileLastPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 4),
    _MobileLastPeriodTxSec_Type()
)
mobileLastPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodTxSec.setStatus("current")
_MobileLastPeriodConnectionsPri_Type = Counter32
_MobileLastPeriodConnectionsPri_Object = MibScalar
mobileLastPeriodConnectionsPri = _MobileLastPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 5),
    _MobileLastPeriodConnectionsPri_Type()
)
mobileLastPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodConnectionsPri.setStatus("current")
_MobileLastPeriodConnectionsSec_Type = Counter32
_MobileLastPeriodConnectionsSec_Object = MibScalar
mobileLastPeriodConnectionsSec = _MobileLastPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 6),
    _MobileLastPeriodConnectionsSec_Type()
)
mobileLastPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodConnectionsSec.setStatus("current")
_MobileLastPeriodOnlinePri_Type = TimeTicks
_MobileLastPeriodOnlinePri_Object = MibScalar
mobileLastPeriodOnlinePri = _MobileLastPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 7),
    _MobileLastPeriodOnlinePri_Type()
)
mobileLastPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodOnlinePri.setStatus("current")
_MobileLastPeriodOnlineSec_Type = TimeTicks
_MobileLastPeriodOnlineSec_Object = MibScalar
mobileLastPeriodOnlineSec = _MobileLastPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 8),
    _MobileLastPeriodOnlineSec_Type()
)
mobileLastPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodOnlineSec.setStatus("current")
_MobileLastPeriodOffline_Type = TimeTicks
_MobileLastPeriodOffline_Object = MibScalar
mobileLastPeriodOffline = _MobileLastPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 9),
    _MobileLastPeriodOffline_Type()
)
mobileLastPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodOffline.setStatus("current")
_MobileLastPeriodCells_Type = Counter32
_MobileLastPeriodCells_Object = MibScalar
mobileLastPeriodCells = _MobileLastPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 10),
    _MobileLastPeriodCells_Type()
)
mobileLastPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodCells.setStatus("current")
_MobileLastPeriodSignalAvg_Type = Integer32
_MobileLastPeriodSignalAvg_Object = MibScalar
mobileLastPeriodSignalAvg = _MobileLastPeriodSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 11),
    _MobileLastPeriodSignalAvg_Type()
)
mobileLastPeriodSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodSignalAvg.setStatus("current")
_MobileLastPeriodSignalMin_Type = Integer32
_MobileLastPeriodSignalMin_Object = MibScalar
mobileLastPeriodSignalMin = _MobileLastPeriodSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 12),
    _MobileLastPeriodSignalMin_Type()
)
mobileLastPeriodSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodSignalMin.setStatus("current")
_MobileLastPeriodSignalMax_Type = Integer32
_MobileLastPeriodSignalMax_Object = MibScalar
mobileLastPeriodSignalMax = _MobileLastPeriodSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 13),
    _MobileLastPeriodSignalMax_Type()
)
mobileLastPeriodSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodSignalMax.setStatus("current")
_MobileLastPeriodDateMin_Type = Counter32
_MobileLastPeriodDateMin_Object = MibScalar
mobileLastPeriodDateMin = _MobileLastPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 14),
    _MobileLastPeriodDateMin_Type()
)
mobileLastPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodDateMin.setStatus("current")
_MobileLastPeriodDateMax_Type = Counter32
_MobileLastPeriodDateMax_Object = MibScalar
mobileLastPeriodDateMax = _MobileLastPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 15),
    _MobileLastPeriodDateMax_Type()
)
mobileLastPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobileLastPeriodDateMax.setStatus("current")
_Mobile2LastPeriodRxPri_Type = Counter32
_Mobile2LastPeriodRxPri_Object = MibScalar
mobile2LastPeriodRxPri = _Mobile2LastPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 101),
    _Mobile2LastPeriodRxPri_Type()
)
mobile2LastPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodRxPri.setStatus("current")
_Mobile2LastPeriodRxSec_Type = Counter32
_Mobile2LastPeriodRxSec_Object = MibScalar
mobile2LastPeriodRxSec = _Mobile2LastPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 102),
    _Mobile2LastPeriodRxSec_Type()
)
mobile2LastPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodRxSec.setStatus("current")
_Mobile2LastPeriodTxPri_Type = Counter32
_Mobile2LastPeriodTxPri_Object = MibScalar
mobile2LastPeriodTxPri = _Mobile2LastPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 103),
    _Mobile2LastPeriodTxPri_Type()
)
mobile2LastPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodTxPri.setStatus("current")
_Mobile2LastPeriodTxSec_Type = Counter32
_Mobile2LastPeriodTxSec_Object = MibScalar
mobile2LastPeriodTxSec = _Mobile2LastPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 104),
    _Mobile2LastPeriodTxSec_Type()
)
mobile2LastPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodTxSec.setStatus("current")
_Mobile2LastPeriodConnectionsPri_Type = Counter32
_Mobile2LastPeriodConnectionsPri_Object = MibScalar
mobile2LastPeriodConnectionsPri = _Mobile2LastPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 105),
    _Mobile2LastPeriodConnectionsPri_Type()
)
mobile2LastPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodConnectionsPri.setStatus("current")
_Mobile2LastPeriodConnectionsSec_Type = Counter32
_Mobile2LastPeriodConnectionsSec_Object = MibScalar
mobile2LastPeriodConnectionsSec = _Mobile2LastPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 106),
    _Mobile2LastPeriodConnectionsSec_Type()
)
mobile2LastPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodConnectionsSec.setStatus("current")
_Mobile2LastPeriodOnlinePri_Type = TimeTicks
_Mobile2LastPeriodOnlinePri_Object = MibScalar
mobile2LastPeriodOnlinePri = _Mobile2LastPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 107),
    _Mobile2LastPeriodOnlinePri_Type()
)
mobile2LastPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodOnlinePri.setStatus("current")
_Mobile2LastPeriodOnlineSec_Type = TimeTicks
_Mobile2LastPeriodOnlineSec_Object = MibScalar
mobile2LastPeriodOnlineSec = _Mobile2LastPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 108),
    _Mobile2LastPeriodOnlineSec_Type()
)
mobile2LastPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodOnlineSec.setStatus("current")
_Mobile2LastPeriodOffline_Type = TimeTicks
_Mobile2LastPeriodOffline_Object = MibScalar
mobile2LastPeriodOffline = _Mobile2LastPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 109),
    _Mobile2LastPeriodOffline_Type()
)
mobile2LastPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodOffline.setStatus("current")
_Mobile2LastPeriodCells_Type = Counter32
_Mobile2LastPeriodCells_Object = MibScalar
mobile2LastPeriodCells = _Mobile2LastPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 110),
    _Mobile2LastPeriodCells_Type()
)
mobile2LastPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodCells.setStatus("current")
_Mobile2LastPeriodSignalAvg_Type = Integer32
_Mobile2LastPeriodSignalAvg_Object = MibScalar
mobile2LastPeriodSignalAvg = _Mobile2LastPeriodSignalAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 111),
    _Mobile2LastPeriodSignalAvg_Type()
)
mobile2LastPeriodSignalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodSignalAvg.setStatus("current")
_Mobile2LastPeriodSignalMin_Type = Integer32
_Mobile2LastPeriodSignalMin_Object = MibScalar
mobile2LastPeriodSignalMin = _Mobile2LastPeriodSignalMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 112),
    _Mobile2LastPeriodSignalMin_Type()
)
mobile2LastPeriodSignalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodSignalMin.setStatus("current")
_Mobile2LastPeriodSignalMax_Type = Integer32
_Mobile2LastPeriodSignalMax_Object = MibScalar
mobile2LastPeriodSignalMax = _Mobile2LastPeriodSignalMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 113),
    _Mobile2LastPeriodSignalMax_Type()
)
mobile2LastPeriodSignalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodSignalMax.setStatus("current")
_Mobile2LastPeriodDateMin_Type = Counter32
_Mobile2LastPeriodDateMin_Object = MibScalar
mobile2LastPeriodDateMin = _Mobile2LastPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 114),
    _Mobile2LastPeriodDateMin_Type()
)
mobile2LastPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodDateMin.setStatus("current")
_Mobile2LastPeriodDateMax_Type = Counter32
_Mobile2LastPeriodDateMax_Object = MibScalar
mobile2LastPeriodDateMax = _Mobile2LastPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 115),
    _Mobile2LastPeriodDateMax_Type()
)
mobile2LastPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobile2LastPeriodDateMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-MOBILE-MIB",
    **{"conel": conel,
       "mobile": mobile,
       "mobileTechnology": mobileTechnology,
       "mobilePLMN": mobilePLMN,
       "mobileCell": mobileCell,
       "mobileChannel": mobileChannel,
       "mobileSignalStrength": mobileSignalStrength,
       "mobileChannelN1": mobileChannelN1,
       "mobileSignalStrengthN1": mobileSignalStrengthN1,
       "mobileChannelN2": mobileChannelN2,
       "mobileSignalStrengthN2": mobileSignalStrengthN2,
       "mobileChannelN3": mobileChannelN3,
       "mobileSignalStrengthN3": mobileSignalStrengthN3,
       "mobileChannelN4": mobileChannelN4,
       "mobileSignalStrengthN4": mobileSignalStrengthN4,
       "mobileChannelN5": mobileChannelN5,
       "mobileSignalStrengthN5": mobileSignalStrengthN5,
       "mobileUpTime": mobileUpTime,
       "mobileConnect": mobileConnect,
       "mobileDisconnect": mobileDisconnect,
       "mobileCard": mobileCard,
       "mobileIPAddress": mobileIPAddress,
       "mobileLatency": mobileLatency,
       "mobileReportPeriod": mobileReportPeriod,
       "mobileRegistration": mobileRegistration,
       "mobileOperator": mobileOperator,
       "mobileLAC": mobileLAC,
       "mobileSignalQuality": mobileSignalQuality,
       "mobileCSQ": mobileCSQ,
       "mobilePNOffset": mobilePNOffset,
       "mobileBand": mobileBand,
       "mobileRSSI": mobileRSSI,
       "mobileRSCP": mobileRSCP,
       "mobileRSRP": mobileRSRP,
       "mobileRSRQ": mobileRSRQ,
       "mobileEcIo": mobileEcIo,
       "mobileNRBand": mobileNRBand,
       "mobileNRChannel": mobileNRChannel,
       "mobileNRRSSI": mobileNRRSSI,
       "mobileNRRSRP": mobileNRRSRP,
       "mobileNRRSRQ": mobileNRRSRQ,
       "mobileNRSINR": mobileNRSINR,
       "mobileSINR": mobileSINR,
       "mobile2Technology": mobile2Technology,
       "mobile2PLMN": mobile2PLMN,
       "mobile2Cell": mobile2Cell,
       "mobile2Channel": mobile2Channel,
       "mobile2SignalStrength": mobile2SignalStrength,
       "mobile2ChannelN1": mobile2ChannelN1,
       "mobile2SignalStrengthN1": mobile2SignalStrengthN1,
       "mobile2ChannelN2": mobile2ChannelN2,
       "mobile2SignalStrengthN2": mobile2SignalStrengthN2,
       "mobile2ChannelN3": mobile2ChannelN3,
       "mobile2SignalStrengthN3": mobile2SignalStrengthN3,
       "mobile2ChannelN4": mobile2ChannelN4,
       "mobile2SignalStrengthN4": mobile2SignalStrengthN4,
       "mobile2ChannelN5": mobile2ChannelN5,
       "mobile2SignalStrengthN5": mobile2SignalStrengthN5,
       "mobile2UpTime": mobile2UpTime,
       "mobile2Connect": mobile2Connect,
       "mobile2Disconnect": mobile2Disconnect,
       "mobile2Card": mobile2Card,
       "mobile2IPAddress": mobile2IPAddress,
       "mobile2Latency": mobile2Latency,
       "mobile2ReportPeriod": mobile2ReportPeriod,
       "mobile2Registration": mobile2Registration,
       "mobile2Operator": mobile2Operator,
       "mobile2LAC": mobile2LAC,
       "mobile2SignalQuality": mobile2SignalQuality,
       "mobile2CSQ": mobile2CSQ,
       "mobile2PNOffset": mobile2PNOffset,
       "mobile2Band": mobile2Band,
       "mobile2RSSI": mobile2RSSI,
       "mobile2RSCP": mobile2RSCP,
       "mobile2RSRP": mobile2RSRP,
       "mobile2RSRQ": mobile2RSRQ,
       "mobile2EcIo": mobile2EcIo,
       "mobile2NRBand": mobile2NRBand,
       "mobile2NRChannel": mobile2NRChannel,
       "mobile2NRRSSI": mobile2NRRSSI,
       "mobile2NRRSRP": mobile2NRRSRP,
       "mobile2NRRSRQ": mobile2NRRSRQ,
       "mobile2NRSINR": mobile2NRSINR,
       "mobile2SINR": mobile2SINR,
       "mobile-2": mobile_2,
       "mobileToday": mobileToday,
       "mobileTodayRxPri": mobileTodayRxPri,
       "mobileTodayRxSec": mobileTodayRxSec,
       "mobileTodayTxPri": mobileTodayTxPri,
       "mobileTodayTxSec": mobileTodayTxSec,
       "mobileTodayConnectionsPri": mobileTodayConnectionsPri,
       "mobileTodayConnectionsSec": mobileTodayConnectionsSec,
       "mobileTodayOnlinePri": mobileTodayOnlinePri,
       "mobileTodayOnlineSec": mobileTodayOnlineSec,
       "mobileTodayOffline": mobileTodayOffline,
       "mobileTodayCells": mobileTodayCells,
       "mobileTodaySignalAvg": mobileTodaySignalAvg,
       "mobileTodaySignalMin": mobileTodaySignalMin,
       "mobileTodaySignalMax": mobileTodaySignalMax,
       "mobileTodayDateMin": mobileTodayDateMin,
       "mobileTodayDateMax": mobileTodayDateMax,
       "mobile2TodayRxPri": mobile2TodayRxPri,
       "mobile2TodayRxSec": mobile2TodayRxSec,
       "mobile2TodayTxPri": mobile2TodayTxPri,
       "mobile2TodayTxSec": mobile2TodayTxSec,
       "mobile2TodayConnectionsPri": mobile2TodayConnectionsPri,
       "mobile2TodayConnectionsSec": mobile2TodayConnectionsSec,
       "mobile2TodayOnlinePri": mobile2TodayOnlinePri,
       "mobile2TodayOnlineSec": mobile2TodayOnlineSec,
       "mobile2TodayOffline": mobile2TodayOffline,
       "mobile2TodayCells": mobile2TodayCells,
       "mobile2TodaySignalAvg": mobile2TodaySignalAvg,
       "mobile2TodaySignalMin": mobile2TodaySignalMin,
       "mobile2TodaySignalMax": mobile2TodaySignalMax,
       "mobile2TodayDateMin": mobile2TodayDateMin,
       "mobile2TodayDateMax": mobile2TodayDateMax,
       "mobileYesterday": mobileYesterday,
       "mobileYesterdayRxPri": mobileYesterdayRxPri,
       "mobileYesterdayRxSec": mobileYesterdayRxSec,
       "mobileYesterdayTxPri": mobileYesterdayTxPri,
       "mobileYesterdayTxSec": mobileYesterdayTxSec,
       "mobileYesterdayConnectionsPri": mobileYesterdayConnectionsPri,
       "mobileYesterdayConnectionsSec": mobileYesterdayConnectionsSec,
       "mobileYesterdayOnlinePri": mobileYesterdayOnlinePri,
       "mobileYesterdayOnlineSec": mobileYesterdayOnlineSec,
       "mobileYesterdayOffline": mobileYesterdayOffline,
       "mobileYesterdayCells": mobileYesterdayCells,
       "mobileYesterdaySignalAvg": mobileYesterdaySignalAvg,
       "mobileYesterdaySignalMin": mobileYesterdaySignalMin,
       "mobileYesterdaySignalMax": mobileYesterdaySignalMax,
       "mobileYesterdayDateMin": mobileYesterdayDateMin,
       "mobileYesterdayDateMax": mobileYesterdayDateMax,
       "mobile2YesterdayRxPri": mobile2YesterdayRxPri,
       "mobile2YesterdayRxSec": mobile2YesterdayRxSec,
       "mobile2YesterdayTxPri": mobile2YesterdayTxPri,
       "mobile2YesterdayTxSec": mobile2YesterdayTxSec,
       "mobile2YesterdayConnectionsPri": mobile2YesterdayConnectionsPri,
       "mobile2YesterdayConnectionsSec": mobile2YesterdayConnectionsSec,
       "mobile2YesterdayOnlinePri": mobile2YesterdayOnlinePri,
       "mobile2YesterdayOnlineSec": mobile2YesterdayOnlineSec,
       "mobile2YesterdayOffline": mobile2YesterdayOffline,
       "mobile2YesterdayCells": mobile2YesterdayCells,
       "mobile2YesterdaySignalAvg": mobile2YesterdaySignalAvg,
       "mobile2YesterdaySignalMin": mobile2YesterdaySignalMin,
       "mobile2YesterdaySignalMax": mobile2YesterdaySignalMax,
       "mobile2YesterdayDateMin": mobile2YesterdayDateMin,
       "mobile2YesterdayDateMax": mobile2YesterdayDateMax,
       "mobileThisWeek": mobileThisWeek,
       "mobileThisWeekRxPri": mobileThisWeekRxPri,
       "mobileThisWeekRxSec": mobileThisWeekRxSec,
       "mobileThisWeekTxPri": mobileThisWeekTxPri,
       "mobileThisWeekTxSec": mobileThisWeekTxSec,
       "mobileThisWeekConnectionsPri": mobileThisWeekConnectionsPri,
       "mobileThisWeekConnectionsSec": mobileThisWeekConnectionsSec,
       "mobileThisWeekOnlinePri": mobileThisWeekOnlinePri,
       "mobileThisWeekOnlineSec": mobileThisWeekOnlineSec,
       "mobileThisWeekOffline": mobileThisWeekOffline,
       "mobileThisWeekCells": mobileThisWeekCells,
       "mobileThisWeekSignalAvg": mobileThisWeekSignalAvg,
       "mobileThisWeekSignalMin": mobileThisWeekSignalMin,
       "mobileThisWeekSignalMax": mobileThisWeekSignalMax,
       "mobileThisWeekDateMin": mobileThisWeekDateMin,
       "mobileThisWeekDateMax": mobileThisWeekDateMax,
       "mobile2ThisWeekRxPri": mobile2ThisWeekRxPri,
       "mobile2ThisWeekRxSec": mobile2ThisWeekRxSec,
       "mobile2ThisWeekTxPri": mobile2ThisWeekTxPri,
       "mobile2ThisWeekTxSec": mobile2ThisWeekTxSec,
       "mobile2ThisWeekConnectionsPri": mobile2ThisWeekConnectionsPri,
       "mobile2ThisWeekConnectionsSec": mobile2ThisWeekConnectionsSec,
       "mobile2ThisWeekOnlinePri": mobile2ThisWeekOnlinePri,
       "mobile2ThisWeekOnlineSec": mobile2ThisWeekOnlineSec,
       "mobile2ThisWeekOffline": mobile2ThisWeekOffline,
       "mobile2ThisWeekCells": mobile2ThisWeekCells,
       "mobile2ThisWeekSignalAvg": mobile2ThisWeekSignalAvg,
       "mobile2ThisWeekSignalMin": mobile2ThisWeekSignalMin,
       "mobile2ThisWeekSignalMax": mobile2ThisWeekSignalMax,
       "mobile2ThisWeekDateMin": mobile2ThisWeekDateMin,
       "mobile2ThisWeekDateMax": mobile2ThisWeekDateMax,
       "mobileLastWeek": mobileLastWeek,
       "mobileLastWeekRxPri": mobileLastWeekRxPri,
       "mobileLastWeekRxSec": mobileLastWeekRxSec,
       "mobileLastWeekTxPri": mobileLastWeekTxPri,
       "mobileLastWeekTxSec": mobileLastWeekTxSec,
       "mobileLastWeekConnectionsPri": mobileLastWeekConnectionsPri,
       "mobileLastWeekConnectionsSec": mobileLastWeekConnectionsSec,
       "mobileLastWeekOnlinePri": mobileLastWeekOnlinePri,
       "mobileLastWeekOnlineSec": mobileLastWeekOnlineSec,
       "mobileLastWeekOffline": mobileLastWeekOffline,
       "mobileLastWeekCells": mobileLastWeekCells,
       "mobileLastWeekSignalAvg": mobileLastWeekSignalAvg,
       "mobileLastWeekSignalMin": mobileLastWeekSignalMin,
       "mobileLastWeekSignalMax": mobileLastWeekSignalMax,
       "mobileLastWeekDateMin": mobileLastWeekDateMin,
       "mobileLastWeekDateMax": mobileLastWeekDateMax,
       "mobile2LastWeekRxPri": mobile2LastWeekRxPri,
       "mobile2LastWeekRxSec": mobile2LastWeekRxSec,
       "mobile2LastWeekTxPri": mobile2LastWeekTxPri,
       "mobile2LastWeekTxSec": mobile2LastWeekTxSec,
       "mobile2LastWeekConnectionsPri": mobile2LastWeekConnectionsPri,
       "mobile2LastWeekConnectionsSec": mobile2LastWeekConnectionsSec,
       "mobile2LastWeekOnlinePri": mobile2LastWeekOnlinePri,
       "mobile2LastWeekOnlineSec": mobile2LastWeekOnlineSec,
       "mobile2LastWeekOffline": mobile2LastWeekOffline,
       "mobile2LastWeekCells": mobile2LastWeekCells,
       "mobile2LastWeekSignalAvg": mobile2LastWeekSignalAvg,
       "mobile2LastWeekSignalMin": mobile2LastWeekSignalMin,
       "mobile2LastWeekSignalMax": mobile2LastWeekSignalMax,
       "mobile2LastWeekDateMin": mobile2LastWeekDateMin,
       "mobile2LastWeekDateMax": mobile2LastWeekDateMax,
       "mobileThisPeriod": mobileThisPeriod,
       "mobileThisPeriodRxPri": mobileThisPeriodRxPri,
       "mobileThisPeriodRxSec": mobileThisPeriodRxSec,
       "mobileThisPeriodTxPri": mobileThisPeriodTxPri,
       "mobileThisPeriodTxSec": mobileThisPeriodTxSec,
       "mobileThisPeriodConnectionsPri": mobileThisPeriodConnectionsPri,
       "mobileThisPeriodConnectionsSec": mobileThisPeriodConnectionsSec,
       "mobileThisPeriodOnlinePri": mobileThisPeriodOnlinePri,
       "mobileThisPeriodOnlineSec": mobileThisPeriodOnlineSec,
       "mobileThisPeriodOffline": mobileThisPeriodOffline,
       "mobileThisPeriodCells": mobileThisPeriodCells,
       "mobileThisPeriodSignalAvg": mobileThisPeriodSignalAvg,
       "mobileThisPeriodSignalMin": mobileThisPeriodSignalMin,
       "mobileThisPeriodSignalMax": mobileThisPeriodSignalMax,
       "mobileThisPeriodDateMin": mobileThisPeriodDateMin,
       "mobileThisPeriodDateMax": mobileThisPeriodDateMax,
       "mobile2ThisPeriodRxPri": mobile2ThisPeriodRxPri,
       "mobile2ThisPeriodRxSec": mobile2ThisPeriodRxSec,
       "mobile2ThisPeriodTxPri": mobile2ThisPeriodTxPri,
       "mobile2ThisPeriodTxSec": mobile2ThisPeriodTxSec,
       "mobile2ThisPeriodConnectionsPri": mobile2ThisPeriodConnectionsPri,
       "mobile2ThisPeriodConnectionsSec": mobile2ThisPeriodConnectionsSec,
       "mobile2ThisPeriodOnlinePri": mobile2ThisPeriodOnlinePri,
       "mobile2ThisPeriodOnlineSec": mobile2ThisPeriodOnlineSec,
       "mobile2ThisPeriodOffline": mobile2ThisPeriodOffline,
       "mobile2ThisPeriodCells": mobile2ThisPeriodCells,
       "mobile2ThisPeriodSignalAvg": mobile2ThisPeriodSignalAvg,
       "mobile2ThisPeriodSignalMin": mobile2ThisPeriodSignalMin,
       "mobile2ThisPeriodSignalMax": mobile2ThisPeriodSignalMax,
       "mobile2ThisPeriodDateMin": mobile2ThisPeriodDateMin,
       "mobile2ThisPeriodDateMax": mobile2ThisPeriodDateMax,
       "mobileLastPeriod": mobileLastPeriod,
       "mobileLastPeriodRxPri": mobileLastPeriodRxPri,
       "mobileLastPeriodRxSec": mobileLastPeriodRxSec,
       "mobileLastPeriodTxPri": mobileLastPeriodTxPri,
       "mobileLastPeriodTxSec": mobileLastPeriodTxSec,
       "mobileLastPeriodConnectionsPri": mobileLastPeriodConnectionsPri,
       "mobileLastPeriodConnectionsSec": mobileLastPeriodConnectionsSec,
       "mobileLastPeriodOnlinePri": mobileLastPeriodOnlinePri,
       "mobileLastPeriodOnlineSec": mobileLastPeriodOnlineSec,
       "mobileLastPeriodOffline": mobileLastPeriodOffline,
       "mobileLastPeriodCells": mobileLastPeriodCells,
       "mobileLastPeriodSignalAvg": mobileLastPeriodSignalAvg,
       "mobileLastPeriodSignalMin": mobileLastPeriodSignalMin,
       "mobileLastPeriodSignalMax": mobileLastPeriodSignalMax,
       "mobileLastPeriodDateMin": mobileLastPeriodDateMin,
       "mobileLastPeriodDateMax": mobileLastPeriodDateMax,
       "mobile2LastPeriodRxPri": mobile2LastPeriodRxPri,
       "mobile2LastPeriodRxSec": mobile2LastPeriodRxSec,
       "mobile2LastPeriodTxPri": mobile2LastPeriodTxPri,
       "mobile2LastPeriodTxSec": mobile2LastPeriodTxSec,
       "mobile2LastPeriodConnectionsPri": mobile2LastPeriodConnectionsPri,
       "mobile2LastPeriodConnectionsSec": mobile2LastPeriodConnectionsSec,
       "mobile2LastPeriodOnlinePri": mobile2LastPeriodOnlinePri,
       "mobile2LastPeriodOnlineSec": mobile2LastPeriodOnlineSec,
       "mobile2LastPeriodOffline": mobile2LastPeriodOffline,
       "mobile2LastPeriodCells": mobile2LastPeriodCells,
       "mobile2LastPeriodSignalAvg": mobile2LastPeriodSignalAvg,
       "mobile2LastPeriodSignalMin": mobile2LastPeriodSignalMin,
       "mobile2LastPeriodSignalMax": mobile2LastPeriodSignalMax,
       "mobile2LastPeriodDateMin": mobile2LastPeriodDateMin,
       "mobile2LastPeriodDateMax": mobile2LastPeriodDateMax}
)
