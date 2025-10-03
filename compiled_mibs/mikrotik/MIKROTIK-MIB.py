# SNMP MIB module (MIKROTIK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mikrotik\MIKROTIK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:36 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mikrotikExperimentalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1)
)
if mibBuilder.loadTexts:
    mikrotikExperimentalModule.setRevisions(
        ("2025-05-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ObjectIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HexInt(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Voltage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Temperature(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Power(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class GDiv100(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-2"


class GDiv1000(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-3"


class IDiv1000(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class BoolValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class IsakmpCookie(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_Mikrotik_ObjectIdentity = ObjectIdentity
mikrotik = _Mikrotik_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988)
)
_MtXRouterOs_ObjectIdentity = ObjectIdentity
mtXRouterOs = _MtXRouterOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1)
)
_MtxrWireless_ObjectIdentity = ObjectIdentity
mtxrWireless = _MtxrWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1)
)
_MtxrWlStatTable_Object = MibTable
mtxrWlStatTable = _MtxrWlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mtxrWlStatTable.setStatus("current")
_MtxrWlStatEntry_Object = MibTableRow
mtxrWlStatEntry = _MtxrWlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1)
)
mtxrWlStatEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlStatIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlStatEntry.setStatus("current")
_MtxrWlStatIndex_Type = ObjectIndex
_MtxrWlStatIndex_Object = MibTableColumn
mtxrWlStatIndex = _MtxrWlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 1),
    _MtxrWlStatIndex_Type()
)
mtxrWlStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlStatIndex.setStatus("current")
_MtxrWlStatTxRate_Type = Gauge32
_MtxrWlStatTxRate_Object = MibTableColumn
mtxrWlStatTxRate = _MtxrWlStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 2),
    _MtxrWlStatTxRate_Type()
)
mtxrWlStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatTxRate.setStatus("current")
_MtxrWlStatRxRate_Type = Gauge32
_MtxrWlStatRxRate_Object = MibTableColumn
mtxrWlStatRxRate = _MtxrWlStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 3),
    _MtxrWlStatRxRate_Type()
)
mtxrWlStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatRxRate.setStatus("current")
_MtxrWlStatStrength_Type = Integer32
_MtxrWlStatStrength_Object = MibTableColumn
mtxrWlStatStrength = _MtxrWlStatStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 4),
    _MtxrWlStatStrength_Type()
)
mtxrWlStatStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatStrength.setStatus("current")
_MtxrWlStatSsid_Type = DisplayString
_MtxrWlStatSsid_Object = MibTableColumn
mtxrWlStatSsid = _MtxrWlStatSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 5),
    _MtxrWlStatSsid_Type()
)
mtxrWlStatSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatSsid.setStatus("current")
_MtxrWlStatBssid_Type = MacAddress
_MtxrWlStatBssid_Object = MibTableColumn
mtxrWlStatBssid = _MtxrWlStatBssid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 6),
    _MtxrWlStatBssid_Type()
)
mtxrWlStatBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatBssid.setStatus("current")
_MtxrWlStatFreq_Type = Integer32
_MtxrWlStatFreq_Object = MibTableColumn
mtxrWlStatFreq = _MtxrWlStatFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 7),
    _MtxrWlStatFreq_Type()
)
mtxrWlStatFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatFreq.setStatus("current")
_MtxrWlStatBand_Type = DisplayString
_MtxrWlStatBand_Object = MibTableColumn
mtxrWlStatBand = _MtxrWlStatBand_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 8),
    _MtxrWlStatBand_Type()
)
mtxrWlStatBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatBand.setStatus("current")
_MtxrWlStatTxCCQ_Type = Counter32
_MtxrWlStatTxCCQ_Object = MibTableColumn
mtxrWlStatTxCCQ = _MtxrWlStatTxCCQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 9),
    _MtxrWlStatTxCCQ_Type()
)
mtxrWlStatTxCCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatTxCCQ.setStatus("current")
_MtxrWlStatRxCCQ_Type = Counter32
_MtxrWlStatRxCCQ_Object = MibTableColumn
mtxrWlStatRxCCQ = _MtxrWlStatRxCCQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 10),
    _MtxrWlStatRxCCQ_Type()
)
mtxrWlStatRxCCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatRxCCQ.setStatus("current")
_MtxrWlRtabTable_Object = MibTable
mtxrWlRtabTable = _MtxrWlRtabTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mtxrWlRtabTable.setStatus("current")
_MtxrWlRtabEntry_Object = MibTableRow
mtxrWlRtabEntry = _MtxrWlRtabEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1)
)
mtxrWlRtabEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlRtabAddr"),
    (0, "MIKROTIK-MIB", "mtxrWlRtabIface"),
)
if mibBuilder.loadTexts:
    mtxrWlRtabEntry.setStatus("current")
_MtxrWlRtabAddr_Type = MacAddress
_MtxrWlRtabAddr_Object = MibTableColumn
mtxrWlRtabAddr = _MtxrWlRtabAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 1),
    _MtxrWlRtabAddr_Type()
)
mtxrWlRtabAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlRtabAddr.setStatus("current")
_MtxrWlRtabIface_Type = ObjectIndex
_MtxrWlRtabIface_Object = MibTableColumn
mtxrWlRtabIface = _MtxrWlRtabIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 2),
    _MtxrWlRtabIface_Type()
)
mtxrWlRtabIface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlRtabIface.setStatus("current")
_MtxrWlRtabStrength_Type = Integer32
_MtxrWlRtabStrength_Object = MibTableColumn
mtxrWlRtabStrength = _MtxrWlRtabStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 3),
    _MtxrWlRtabStrength_Type()
)
mtxrWlRtabStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabStrength.setStatus("current")
_MtxrWlRtabTxBytes_Type = Counter32
_MtxrWlRtabTxBytes_Object = MibTableColumn
mtxrWlRtabTxBytes = _MtxrWlRtabTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 4),
    _MtxrWlRtabTxBytes_Type()
)
mtxrWlRtabTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxBytes.setStatus("current")
_MtxrWlRtabRxBytes_Type = Counter32
_MtxrWlRtabRxBytes_Object = MibTableColumn
mtxrWlRtabRxBytes = _MtxrWlRtabRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 5),
    _MtxrWlRtabRxBytes_Type()
)
mtxrWlRtabRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxBytes.setStatus("current")
_MtxrWlRtabTxPackets_Type = Counter32
_MtxrWlRtabTxPackets_Object = MibTableColumn
mtxrWlRtabTxPackets = _MtxrWlRtabTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 6),
    _MtxrWlRtabTxPackets_Type()
)
mtxrWlRtabTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxPackets.setStatus("current")
_MtxrWlRtabRxPackets_Type = Counter32
_MtxrWlRtabRxPackets_Object = MibTableColumn
mtxrWlRtabRxPackets = _MtxrWlRtabRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 7),
    _MtxrWlRtabRxPackets_Type()
)
mtxrWlRtabRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxPackets.setStatus("current")
_MtxrWlRtabTxRate_Type = Gauge32
_MtxrWlRtabTxRate_Object = MibTableColumn
mtxrWlRtabTxRate = _MtxrWlRtabTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 8),
    _MtxrWlRtabTxRate_Type()
)
mtxrWlRtabTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxRate.setStatus("current")
_MtxrWlRtabRxRate_Type = Gauge32
_MtxrWlRtabRxRate_Object = MibTableColumn
mtxrWlRtabRxRate = _MtxrWlRtabRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 9),
    _MtxrWlRtabRxRate_Type()
)
mtxrWlRtabRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxRate.setStatus("current")
_MtxrWlRtabRouterOSVersion_Type = DisplayString
_MtxrWlRtabRouterOSVersion_Object = MibTableColumn
mtxrWlRtabRouterOSVersion = _MtxrWlRtabRouterOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 10),
    _MtxrWlRtabRouterOSVersion_Type()
)
mtxrWlRtabRouterOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRouterOSVersion.setStatus("current")
_MtxrWlRtabUptime_Type = TimeTicks
_MtxrWlRtabUptime_Object = MibTableColumn
mtxrWlRtabUptime = _MtxrWlRtabUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 11),
    _MtxrWlRtabUptime_Type()
)
mtxrWlRtabUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabUptime.setStatus("current")
_MtxrWlRtabSignalToNoise_Type = Integer32
_MtxrWlRtabSignalToNoise_Object = MibTableColumn
mtxrWlRtabSignalToNoise = _MtxrWlRtabSignalToNoise_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 12),
    _MtxrWlRtabSignalToNoise_Type()
)
mtxrWlRtabSignalToNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabSignalToNoise.setStatus("current")
_MtxrWlRtabTxStrengthCh0_Type = Integer32
_MtxrWlRtabTxStrengthCh0_Object = MibTableColumn
mtxrWlRtabTxStrengthCh0 = _MtxrWlRtabTxStrengthCh0_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 13),
    _MtxrWlRtabTxStrengthCh0_Type()
)
mtxrWlRtabTxStrengthCh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh0.setStatus("current")
_MtxrWlRtabRxStrengthCh0_Type = Integer32
_MtxrWlRtabRxStrengthCh0_Object = MibTableColumn
mtxrWlRtabRxStrengthCh0 = _MtxrWlRtabRxStrengthCh0_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 14),
    _MtxrWlRtabRxStrengthCh0_Type()
)
mtxrWlRtabRxStrengthCh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh0.setStatus("current")
_MtxrWlRtabTxStrengthCh1_Type = Integer32
_MtxrWlRtabTxStrengthCh1_Object = MibTableColumn
mtxrWlRtabTxStrengthCh1 = _MtxrWlRtabTxStrengthCh1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 15),
    _MtxrWlRtabTxStrengthCh1_Type()
)
mtxrWlRtabTxStrengthCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh1.setStatus("current")
_MtxrWlRtabRxStrengthCh1_Type = Integer32
_MtxrWlRtabRxStrengthCh1_Object = MibTableColumn
mtxrWlRtabRxStrengthCh1 = _MtxrWlRtabRxStrengthCh1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 16),
    _MtxrWlRtabRxStrengthCh1_Type()
)
mtxrWlRtabRxStrengthCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh1.setStatus("current")
_MtxrWlRtabTxStrengthCh2_Type = Integer32
_MtxrWlRtabTxStrengthCh2_Object = MibTableColumn
mtxrWlRtabTxStrengthCh2 = _MtxrWlRtabTxStrengthCh2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 17),
    _MtxrWlRtabTxStrengthCh2_Type()
)
mtxrWlRtabTxStrengthCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh2.setStatus("current")
_MtxrWlRtabRxStrengthCh2_Type = Integer32
_MtxrWlRtabRxStrengthCh2_Object = MibTableColumn
mtxrWlRtabRxStrengthCh2 = _MtxrWlRtabRxStrengthCh2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 18),
    _MtxrWlRtabRxStrengthCh2_Type()
)
mtxrWlRtabRxStrengthCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh2.setStatus("current")
_MtxrWlRtabTxStrength_Type = Integer32
_MtxrWlRtabTxStrength_Object = MibTableColumn
mtxrWlRtabTxStrength = _MtxrWlRtabTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 19),
    _MtxrWlRtabTxStrength_Type()
)
mtxrWlRtabTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrength.setStatus("current")
_MtxrWlRtabRadioName_Type = DisplayString
_MtxrWlRtabRadioName_Object = MibTableColumn
mtxrWlRtabRadioName = _MtxrWlRtabRadioName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 20),
    _MtxrWlRtabRadioName_Type()
)
mtxrWlRtabRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRadioName.setStatus("current")
_MtxrWlApTable_Object = MibTable
mtxrWlApTable = _MtxrWlApTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mtxrWlApTable.setStatus("current")
_MtxrWlApEntry_Object = MibTableRow
mtxrWlApEntry = _MtxrWlApEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1)
)
mtxrWlApEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlApIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlApEntry.setStatus("current")
_MtxrWlApIndex_Type = ObjectIndex
_MtxrWlApIndex_Object = MibTableColumn
mtxrWlApIndex = _MtxrWlApIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 1),
    _MtxrWlApIndex_Type()
)
mtxrWlApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlApIndex.setStatus("current")
_MtxrWlApTxRate_Type = Gauge32
_MtxrWlApTxRate_Object = MibTableColumn
mtxrWlApTxRate = _MtxrWlApTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 2),
    _MtxrWlApTxRate_Type()
)
mtxrWlApTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApTxRate.setStatus("current")
_MtxrWlApRxRate_Type = Gauge32
_MtxrWlApRxRate_Object = MibTableColumn
mtxrWlApRxRate = _MtxrWlApRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 3),
    _MtxrWlApRxRate_Type()
)
mtxrWlApRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApRxRate.setStatus("current")
_MtxrWlApSsid_Type = DisplayString
_MtxrWlApSsid_Object = MibTableColumn
mtxrWlApSsid = _MtxrWlApSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 4),
    _MtxrWlApSsid_Type()
)
mtxrWlApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApSsid.setStatus("current")
_MtxrWlApBssid_Type = MacAddress
_MtxrWlApBssid_Object = MibTableColumn
mtxrWlApBssid = _MtxrWlApBssid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 5),
    _MtxrWlApBssid_Type()
)
mtxrWlApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApBssid.setStatus("current")
_MtxrWlApClientCount_Type = Counter32
_MtxrWlApClientCount_Object = MibTableColumn
mtxrWlApClientCount = _MtxrWlApClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 6),
    _MtxrWlApClientCount_Type()
)
mtxrWlApClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApClientCount.setStatus("current")
_MtxrWlApFreq_Type = Integer32
_MtxrWlApFreq_Object = MibTableColumn
mtxrWlApFreq = _MtxrWlApFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 7),
    _MtxrWlApFreq_Type()
)
mtxrWlApFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApFreq.setStatus("current")
_MtxrWlApBand_Type = DisplayString
_MtxrWlApBand_Object = MibTableColumn
mtxrWlApBand = _MtxrWlApBand_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 8),
    _MtxrWlApBand_Type()
)
mtxrWlApBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApBand.setStatus("current")
_MtxrWlApNoiseFloor_Type = Integer32
_MtxrWlApNoiseFloor_Object = MibTableColumn
mtxrWlApNoiseFloor = _MtxrWlApNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 9),
    _MtxrWlApNoiseFloor_Type()
)
mtxrWlApNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApNoiseFloor.setStatus("current")
_MtxrWlApOverallTxCCQ_Type = Counter32
_MtxrWlApOverallTxCCQ_Object = MibTableColumn
mtxrWlApOverallTxCCQ = _MtxrWlApOverallTxCCQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 10),
    _MtxrWlApOverallTxCCQ_Type()
)
mtxrWlApOverallTxCCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApOverallTxCCQ.setStatus("current")
_MtxrWlApAuthClientCount_Type = Counter32
_MtxrWlApAuthClientCount_Object = MibTableColumn
mtxrWlApAuthClientCount = _MtxrWlApAuthClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 11),
    _MtxrWlApAuthClientCount_Type()
)
mtxrWlApAuthClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApAuthClientCount.setStatus("current")
_MtxrWlRtabEntryCount_Type = Gauge32
_MtxrWlRtabEntryCount_Object = MibScalar
mtxrWlRtabEntryCount = _MtxrWlRtabEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 4),
    _MtxrWlRtabEntryCount_Type()
)
mtxrWlRtabEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabEntryCount.setStatus("current")
_MtxrWlCMRtabTable_Object = MibTable
mtxrWlCMRtabTable = _MtxrWlCMRtabTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mtxrWlCMRtabTable.setStatus("current")
_MtxrWlCMRtabEntry_Object = MibTableRow
mtxrWlCMRtabEntry = _MtxrWlCMRtabEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1)
)
mtxrWlCMRtabEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlCMRtabAddr"),
    (0, "MIKROTIK-MIB", "mtxrWlCMRtabIface"),
)
if mibBuilder.loadTexts:
    mtxrWlCMRtabEntry.setStatus("current")
_MtxrWlCMRtabAddr_Type = MacAddress
_MtxrWlCMRtabAddr_Object = MibTableColumn
mtxrWlCMRtabAddr = _MtxrWlCMRtabAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 1),
    _MtxrWlCMRtabAddr_Type()
)
mtxrWlCMRtabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabAddr.setStatus("current")
_MtxrWlCMRtabIface_Type = ObjectIndex
_MtxrWlCMRtabIface_Object = MibTableColumn
mtxrWlCMRtabIface = _MtxrWlCMRtabIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 2),
    _MtxrWlCMRtabIface_Type()
)
mtxrWlCMRtabIface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlCMRtabIface.setStatus("current")
_MtxrWlCMRtabUptime_Type = TimeTicks
_MtxrWlCMRtabUptime_Object = MibTableColumn
mtxrWlCMRtabUptime = _MtxrWlCMRtabUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 3),
    _MtxrWlCMRtabUptime_Type()
)
mtxrWlCMRtabUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabUptime.setStatus("current")
_MtxrWlCMRtabTxBytes_Type = Counter32
_MtxrWlCMRtabTxBytes_Object = MibTableColumn
mtxrWlCMRtabTxBytes = _MtxrWlCMRtabTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 4),
    _MtxrWlCMRtabTxBytes_Type()
)
mtxrWlCMRtabTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxBytes.setStatus("current")
_MtxrWlCMRtabRxBytes_Type = Counter32
_MtxrWlCMRtabRxBytes_Object = MibTableColumn
mtxrWlCMRtabRxBytes = _MtxrWlCMRtabRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 5),
    _MtxrWlCMRtabRxBytes_Type()
)
mtxrWlCMRtabRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxBytes.setStatus("current")
_MtxrWlCMRtabTxPackets_Type = Counter32
_MtxrWlCMRtabTxPackets_Object = MibTableColumn
mtxrWlCMRtabTxPackets = _MtxrWlCMRtabTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 6),
    _MtxrWlCMRtabTxPackets_Type()
)
mtxrWlCMRtabTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxPackets.setStatus("current")
_MtxrWlCMRtabRxPackets_Type = Counter32
_MtxrWlCMRtabRxPackets_Object = MibTableColumn
mtxrWlCMRtabRxPackets = _MtxrWlCMRtabRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 7),
    _MtxrWlCMRtabRxPackets_Type()
)
mtxrWlCMRtabRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxPackets.setStatus("current")
_MtxrWlCMRtabTxRate_Type = Gauge32
_MtxrWlCMRtabTxRate_Object = MibTableColumn
mtxrWlCMRtabTxRate = _MtxrWlCMRtabTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 8),
    _MtxrWlCMRtabTxRate_Type()
)
mtxrWlCMRtabTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxRate.setStatus("current")
_MtxrWlCMRtabRxRate_Type = Gauge32
_MtxrWlCMRtabRxRate_Object = MibTableColumn
mtxrWlCMRtabRxRate = _MtxrWlCMRtabRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 9),
    _MtxrWlCMRtabRxRate_Type()
)
mtxrWlCMRtabRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxRate.setStatus("current")
_MtxrWlCMRtabTxStrength_Type = Integer32
_MtxrWlCMRtabTxStrength_Object = MibTableColumn
mtxrWlCMRtabTxStrength = _MtxrWlCMRtabTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 10),
    _MtxrWlCMRtabTxStrength_Type()
)
mtxrWlCMRtabTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxStrength.setStatus("current")
_MtxrWlCMRtabRxStrength_Type = Integer32
_MtxrWlCMRtabRxStrength_Object = MibTableColumn
mtxrWlCMRtabRxStrength = _MtxrWlCMRtabRxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 11),
    _MtxrWlCMRtabRxStrength_Type()
)
mtxrWlCMRtabRxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxStrength.setStatus("current")
_MtxrWlCMRtabSsid_Type = DisplayString
_MtxrWlCMRtabSsid_Object = MibTableColumn
mtxrWlCMRtabSsid = _MtxrWlCMRtabSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 12),
    _MtxrWlCMRtabSsid_Type()
)
mtxrWlCMRtabSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabSsid.setStatus("current")
_MtxrWlCMRtabEapIdent_Type = DisplayString
_MtxrWlCMRtabEapIdent_Object = MibTableColumn
mtxrWlCMRtabEapIdent = _MtxrWlCMRtabEapIdent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 13),
    _MtxrWlCMRtabEapIdent_Type()
)
mtxrWlCMRtabEapIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabEapIdent.setStatus("current")
_MtxrWlCMRtabEntryCount_Type = Gauge32
_MtxrWlCMRtabEntryCount_Object = MibScalar
mtxrWlCMRtabEntryCount = _MtxrWlCMRtabEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 6),
    _MtxrWlCMRtabEntryCount_Type()
)
mtxrWlCMRtabEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabEntryCount.setStatus("current")
_MtxrWlCMTable_Object = MibTable
mtxrWlCMTable = _MtxrWlCMTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mtxrWlCMTable.setStatus("current")
_MtxrWlCMEntry_Object = MibTableRow
mtxrWlCMEntry = _MtxrWlCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1)
)
mtxrWlCMEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlCMIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlCMEntry.setStatus("current")
_MtxrWlCMIndex_Type = ObjectIndex
_MtxrWlCMIndex_Object = MibTableColumn
mtxrWlCMIndex = _MtxrWlCMIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1, 1),
    _MtxrWlCMIndex_Type()
)
mtxrWlCMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlCMIndex.setStatus("current")
_MtxrWlCMRegClientCount_Type = Counter32
_MtxrWlCMRegClientCount_Object = MibTableColumn
mtxrWlCMRegClientCount = _MtxrWlCMRegClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1, 2),
    _MtxrWlCMRegClientCount_Type()
)
mtxrWlCMRegClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRegClientCount.setStatus("current")
_MtxrWlCMAuthClientCount_Type = Counter32
_MtxrWlCMAuthClientCount_Object = MibTableColumn
mtxrWlCMAuthClientCount = _MtxrWlCMAuthClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1, 3),
    _MtxrWlCMAuthClientCount_Type()
)
mtxrWlCMAuthClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMAuthClientCount.setStatus("current")
_MtxrWlCMState_Type = DisplayString
_MtxrWlCMState_Object = MibTableColumn
mtxrWlCMState = _MtxrWlCMState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1, 4),
    _MtxrWlCMState_Type()
)
mtxrWlCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMState.setStatus("current")
_MtxrWlCMChannel_Type = DisplayString
_MtxrWlCMChannel_Object = MibTableColumn
mtxrWlCMChannel = _MtxrWlCMChannel_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 7, 1, 5),
    _MtxrWlCMChannel_Type()
)
mtxrWlCMChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMChannel.setStatus("current")
_MtxrWl60GTable_Object = MibTable
mtxrWl60GTable = _MtxrWl60GTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mtxrWl60GTable.setStatus("current")
_MtxrWl60GEntry_Object = MibTableRow
mtxrWl60GEntry = _MtxrWl60GEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1)
)
mtxrWl60GEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWl60GIndex"),
)
if mibBuilder.loadTexts:
    mtxrWl60GEntry.setStatus("current")
_MtxrWl60GIndex_Type = ObjectIndex
_MtxrWl60GIndex_Object = MibTableColumn
mtxrWl60GIndex = _MtxrWl60GIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 1),
    _MtxrWl60GIndex_Type()
)
mtxrWl60GIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWl60GIndex.setStatus("current")


class _MtxrWl60GMode_Type(Integer32):
    """Custom type mtxrWl60GMode based on Integer32"""
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
        *(("apBridge", 0),
          ("stationBridge", 1),
          ("sniff", 2),
          ("bridge", 3))
    )


_MtxrWl60GMode_Type.__name__ = "Integer32"
_MtxrWl60GMode_Object = MibTableColumn
mtxrWl60GMode = _MtxrWl60GMode_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 2),
    _MtxrWl60GMode_Type()
)
mtxrWl60GMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GMode.setStatus("current")
_MtxrWl60GSsid_Type = DisplayString
_MtxrWl60GSsid_Object = MibTableColumn
mtxrWl60GSsid = _MtxrWl60GSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 3),
    _MtxrWl60GSsid_Type()
)
mtxrWl60GSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GSsid.setStatus("current")
_MtxrWl60GConnected_Type = BoolValue
_MtxrWl60GConnected_Object = MibTableColumn
mtxrWl60GConnected = _MtxrWl60GConnected_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 4),
    _MtxrWl60GConnected_Type()
)
mtxrWl60GConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GConnected.setStatus("current")
_MtxrWl60GRemote_Type = MacAddress
_MtxrWl60GRemote_Object = MibTableColumn
mtxrWl60GRemote = _MtxrWl60GRemote_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 5),
    _MtxrWl60GRemote_Type()
)
mtxrWl60GRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GRemote.setStatus("current")
_MtxrWl60GFreq_Type = Integer32
_MtxrWl60GFreq_Object = MibTableColumn
mtxrWl60GFreq = _MtxrWl60GFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 6),
    _MtxrWl60GFreq_Type()
)
mtxrWl60GFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GFreq.setStatus("current")
_MtxrWl60GMcs_Type = Integer32
_MtxrWl60GMcs_Object = MibTableColumn
mtxrWl60GMcs = _MtxrWl60GMcs_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 7),
    _MtxrWl60GMcs_Type()
)
mtxrWl60GMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GMcs.setStatus("current")
_MtxrWl60GSignal_Type = Integer32
_MtxrWl60GSignal_Object = MibTableColumn
mtxrWl60GSignal = _MtxrWl60GSignal_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 8),
    _MtxrWl60GSignal_Type()
)
mtxrWl60GSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GSignal.setStatus("current")
_MtxrWl60GTxSector_Type = Integer32
_MtxrWl60GTxSector_Object = MibTableColumn
mtxrWl60GTxSector = _MtxrWl60GTxSector_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 9),
    _MtxrWl60GTxSector_Type()
)
mtxrWl60GTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GTxSector.setStatus("current")
_MtxrWl60GTxSectorInfo_Type = DisplayString
_MtxrWl60GTxSectorInfo_Object = MibTableColumn
mtxrWl60GTxSectorInfo = _MtxrWl60GTxSectorInfo_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 11),
    _MtxrWl60GTxSectorInfo_Type()
)
mtxrWl60GTxSectorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GTxSectorInfo.setStatus("current")
_MtxrWl60GRssi_Type = Integer32
_MtxrWl60GRssi_Object = MibTableColumn
mtxrWl60GRssi = _MtxrWl60GRssi_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 12),
    _MtxrWl60GRssi_Type()
)
mtxrWl60GRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GRssi.setStatus("current")
_MtxrWl60GPhyRate_Type = Gauge32
_MtxrWl60GPhyRate_Object = MibTableColumn
mtxrWl60GPhyRate = _MtxrWl60GPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 8, 1, 13),
    _MtxrWl60GPhyRate_Type()
)
mtxrWl60GPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GPhyRate.setStatus("current")
_MtxrWl60GStaTable_Object = MibTable
mtxrWl60GStaTable = _MtxrWl60GStaTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mtxrWl60GStaTable.setStatus("current")
_MtxrWl60GStaEntry_Object = MibTableRow
mtxrWl60GStaEntry = _MtxrWl60GStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1)
)
mtxrWl60GStaEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWl60GStaIndex"),
)
if mibBuilder.loadTexts:
    mtxrWl60GStaEntry.setStatus("current")
_MtxrWl60GStaIndex_Type = ObjectIndex
_MtxrWl60GStaIndex_Object = MibTableColumn
mtxrWl60GStaIndex = _MtxrWl60GStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 1),
    _MtxrWl60GStaIndex_Type()
)
mtxrWl60GStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWl60GStaIndex.setStatus("current")
_MtxrWl60GStaConnected_Type = BoolValue
_MtxrWl60GStaConnected_Object = MibTableColumn
mtxrWl60GStaConnected = _MtxrWl60GStaConnected_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 2),
    _MtxrWl60GStaConnected_Type()
)
mtxrWl60GStaConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaConnected.setStatus("current")
_MtxrWl60GStaRemote_Type = MacAddress
_MtxrWl60GStaRemote_Object = MibTableColumn
mtxrWl60GStaRemote = _MtxrWl60GStaRemote_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 3),
    _MtxrWl60GStaRemote_Type()
)
mtxrWl60GStaRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaRemote.setStatus("current")
_MtxrWl60GStaMcs_Type = Integer32
_MtxrWl60GStaMcs_Object = MibTableColumn
mtxrWl60GStaMcs = _MtxrWl60GStaMcs_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 4),
    _MtxrWl60GStaMcs_Type()
)
mtxrWl60GStaMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaMcs.setStatus("current")
_MtxrWl60GStaSignal_Type = Integer32
_MtxrWl60GStaSignal_Object = MibTableColumn
mtxrWl60GStaSignal = _MtxrWl60GStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 5),
    _MtxrWl60GStaSignal_Type()
)
mtxrWl60GStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaSignal.setStatus("current")
_MtxrWl60GStaTxSector_Type = Integer32
_MtxrWl60GStaTxSector_Object = MibTableColumn
mtxrWl60GStaTxSector = _MtxrWl60GStaTxSector_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 6),
    _MtxrWl60GStaTxSector_Type()
)
mtxrWl60GStaTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaTxSector.setStatus("current")
_MtxrWl60GStaPhyRate_Type = Gauge32
_MtxrWl60GStaPhyRate_Object = MibTableColumn
mtxrWl60GStaPhyRate = _MtxrWl60GStaPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 8),
    _MtxrWl60GStaPhyRate_Type()
)
mtxrWl60GStaPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaPhyRate.setStatus("current")
_MtxrWl60GStaRssi_Type = Integer32
_MtxrWl60GStaRssi_Object = MibTableColumn
mtxrWl60GStaRssi = _MtxrWl60GStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 9),
    _MtxrWl60GStaRssi_Type()
)
mtxrWl60GStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaRssi.setStatus("current")
_MtxrWl60GStaDistance_Type = Integer32
_MtxrWl60GStaDistance_Object = MibTableColumn
mtxrWl60GStaDistance = _MtxrWl60GStaDistance_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 9, 1, 10),
    _MtxrWl60GStaDistance_Type()
)
mtxrWl60GStaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWl60GStaDistance.setStatus("current")
_MtxrWlCMREntryCount_Type = Gauge32
_MtxrWlCMREntryCount_Object = MibScalar
mtxrWlCMREntryCount = _MtxrWlCMREntryCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 10),
    _MtxrWlCMREntryCount_Type()
)
mtxrWlCMREntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMREntryCount.setStatus("current")
_MtxrWlCMRemoteTable_Object = MibTable
mtxrWlCMRemoteTable = _MtxrWlCMRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mtxrWlCMRemoteTable.setStatus("current")
_MtxrWlCMRemoteEntry_Object = MibTableRow
mtxrWlCMRemoteEntry = _MtxrWlCMRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1)
)
mtxrWlCMRemoteEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlCMRemoteIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlCMRemoteEntry.setStatus("current")
_MtxrWlCMRemoteIndex_Type = ObjectIndex
_MtxrWlCMRemoteIndex_Object = MibTableColumn
mtxrWlCMRemoteIndex = _MtxrWlCMRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1, 1),
    _MtxrWlCMRemoteIndex_Type()
)
mtxrWlCMRemoteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlCMRemoteIndex.setStatus("current")
_MtxrWlCMRemoteName_Type = DisplayString
_MtxrWlCMRemoteName_Object = MibTableColumn
mtxrWlCMRemoteName = _MtxrWlCMRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1, 2),
    _MtxrWlCMRemoteName_Type()
)
mtxrWlCMRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRemoteName.setStatus("current")
_MtxrWlCMRemoteState_Type = DisplayString
_MtxrWlCMRemoteState_Object = MibTableColumn
mtxrWlCMRemoteState = _MtxrWlCMRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1, 3),
    _MtxrWlCMRemoteState_Type()
)
mtxrWlCMRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRemoteState.setStatus("current")
_MtxrWlCMRemoteAddress_Type = DisplayString
_MtxrWlCMRemoteAddress_Object = MibTableColumn
mtxrWlCMRemoteAddress = _MtxrWlCMRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1, 4),
    _MtxrWlCMRemoteAddress_Type()
)
mtxrWlCMRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRemoteAddress.setStatus("current")
_MtxrWlCMRemoteRadios_Type = Counter32
_MtxrWlCMRemoteRadios_Object = MibTableColumn
mtxrWlCMRemoteRadios = _MtxrWlCMRemoteRadios_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 11, 1, 5),
    _MtxrWlCMRemoteRadios_Type()
)
mtxrWlCMRemoteRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRemoteRadios.setStatus("current")
_MtxrQueues_ObjectIdentity = ObjectIdentity
mtxrQueues = _MtxrQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2)
)
_MtxrQueueSimpleTable_Object = MibTable
mtxrQueueSimpleTable = _MtxrQueueSimpleTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mtxrQueueSimpleTable.setStatus("current")
_MtxrQueueSimpleEntry_Object = MibTableRow
mtxrQueueSimpleEntry = _MtxrQueueSimpleEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1)
)
mtxrQueueSimpleEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrQueueSimpleIndex"),
)
if mibBuilder.loadTexts:
    mtxrQueueSimpleEntry.setStatus("current")
_MtxrQueueSimpleIndex_Type = ObjectIndex
_MtxrQueueSimpleIndex_Object = MibTableColumn
mtxrQueueSimpleIndex = _MtxrQueueSimpleIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 1),
    _MtxrQueueSimpleIndex_Type()
)
mtxrQueueSimpleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrQueueSimpleIndex.setStatus("current")
_MtxrQueueSimpleName_Type = DisplayString
_MtxrQueueSimpleName_Object = MibTableColumn
mtxrQueueSimpleName = _MtxrQueueSimpleName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 2),
    _MtxrQueueSimpleName_Type()
)
mtxrQueueSimpleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleName.setStatus("current")
_MtxrQueueSimpleSrcAddr_Type = IpAddress
_MtxrQueueSimpleSrcAddr_Object = MibTableColumn
mtxrQueueSimpleSrcAddr = _MtxrQueueSimpleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 3),
    _MtxrQueueSimpleSrcAddr_Type()
)
mtxrQueueSimpleSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleSrcAddr.setStatus("current")
_MtxrQueueSimpleSrcMask_Type = IpAddress
_MtxrQueueSimpleSrcMask_Object = MibTableColumn
mtxrQueueSimpleSrcMask = _MtxrQueueSimpleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 4),
    _MtxrQueueSimpleSrcMask_Type()
)
mtxrQueueSimpleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleSrcMask.setStatus("current")
_MtxrQueueSimpleDstAddr_Type = IpAddress
_MtxrQueueSimpleDstAddr_Object = MibTableColumn
mtxrQueueSimpleDstAddr = _MtxrQueueSimpleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 5),
    _MtxrQueueSimpleDstAddr_Type()
)
mtxrQueueSimpleDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDstAddr.setStatus("current")
_MtxrQueueSimpleDstMask_Type = IpAddress
_MtxrQueueSimpleDstMask_Object = MibTableColumn
mtxrQueueSimpleDstMask = _MtxrQueueSimpleDstMask_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 6),
    _MtxrQueueSimpleDstMask_Type()
)
mtxrQueueSimpleDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDstMask.setStatus("current")
_MtxrQueueSimpleIface_Type = ObjectIndex
_MtxrQueueSimpleIface_Object = MibTableColumn
mtxrQueueSimpleIface = _MtxrQueueSimpleIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 7),
    _MtxrQueueSimpleIface_Type()
)
mtxrQueueSimpleIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleIface.setStatus("current")
_MtxrQueueSimpleBytesIn_Type = Counter64
_MtxrQueueSimpleBytesIn_Object = MibTableColumn
mtxrQueueSimpleBytesIn = _MtxrQueueSimpleBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 8),
    _MtxrQueueSimpleBytesIn_Type()
)
mtxrQueueSimpleBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleBytesIn.setStatus("current")
_MtxrQueueSimpleBytesOut_Type = Counter64
_MtxrQueueSimpleBytesOut_Object = MibTableColumn
mtxrQueueSimpleBytesOut = _MtxrQueueSimpleBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 9),
    _MtxrQueueSimpleBytesOut_Type()
)
mtxrQueueSimpleBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleBytesOut.setStatus("current")
_MtxrQueueSimplePacketsIn_Type = Counter32
_MtxrQueueSimplePacketsIn_Object = MibTableColumn
mtxrQueueSimplePacketsIn = _MtxrQueueSimplePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 10),
    _MtxrQueueSimplePacketsIn_Type()
)
mtxrQueueSimplePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePacketsIn.setStatus("current")
_MtxrQueueSimplePacketsOut_Type = Counter32
_MtxrQueueSimplePacketsOut_Object = MibTableColumn
mtxrQueueSimplePacketsOut = _MtxrQueueSimplePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 11),
    _MtxrQueueSimplePacketsOut_Type()
)
mtxrQueueSimplePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePacketsOut.setStatus("current")
_MtxrQueueSimplePCQQueuesIn_Type = Counter32
_MtxrQueueSimplePCQQueuesIn_Object = MibTableColumn
mtxrQueueSimplePCQQueuesIn = _MtxrQueueSimplePCQQueuesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 12),
    _MtxrQueueSimplePCQQueuesIn_Type()
)
mtxrQueueSimplePCQQueuesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePCQQueuesIn.setStatus("current")
_MtxrQueueSimplePCQQueuesOut_Type = Counter32
_MtxrQueueSimplePCQQueuesOut_Object = MibTableColumn
mtxrQueueSimplePCQQueuesOut = _MtxrQueueSimplePCQQueuesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 13),
    _MtxrQueueSimplePCQQueuesOut_Type()
)
mtxrQueueSimplePCQQueuesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePCQQueuesOut.setStatus("current")
_MtxrQueueSimpleDroppedIn_Type = Counter32
_MtxrQueueSimpleDroppedIn_Object = MibTableColumn
mtxrQueueSimpleDroppedIn = _MtxrQueueSimpleDroppedIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 14),
    _MtxrQueueSimpleDroppedIn_Type()
)
mtxrQueueSimpleDroppedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDroppedIn.setStatus("current")
_MtxrQueueSimpleDroppedOut_Type = Counter32
_MtxrQueueSimpleDroppedOut_Object = MibTableColumn
mtxrQueueSimpleDroppedOut = _MtxrQueueSimpleDroppedOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 15),
    _MtxrQueueSimpleDroppedOut_Type()
)
mtxrQueueSimpleDroppedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDroppedOut.setStatus("current")
_MtxrQueueTreeTable_Object = MibTable
mtxrQueueTreeTable = _MtxrQueueTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mtxrQueueTreeTable.setStatus("current")
_MtxrQueueTreeEntry_Object = MibTableRow
mtxrQueueTreeEntry = _MtxrQueueTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1)
)
mtxrQueueTreeEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrQueueTreeIndex"),
)
if mibBuilder.loadTexts:
    mtxrQueueTreeEntry.setStatus("current")
_MtxrQueueTreeIndex_Type = ObjectIndex
_MtxrQueueTreeIndex_Object = MibTableColumn
mtxrQueueTreeIndex = _MtxrQueueTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 1),
    _MtxrQueueTreeIndex_Type()
)
mtxrQueueTreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrQueueTreeIndex.setStatus("current")
_MtxrQueueTreeName_Type = DisplayString
_MtxrQueueTreeName_Object = MibTableColumn
mtxrQueueTreeName = _MtxrQueueTreeName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 2),
    _MtxrQueueTreeName_Type()
)
mtxrQueueTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeName.setStatus("current")
_MtxrQueueTreeFlow_Type = DisplayString
_MtxrQueueTreeFlow_Object = MibTableColumn
mtxrQueueTreeFlow = _MtxrQueueTreeFlow_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 3),
    _MtxrQueueTreeFlow_Type()
)
mtxrQueueTreeFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeFlow.setStatus("current")
_MtxrQueueTreeParentIndex_Type = ObjectIndex
_MtxrQueueTreeParentIndex_Object = MibTableColumn
mtxrQueueTreeParentIndex = _MtxrQueueTreeParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 4),
    _MtxrQueueTreeParentIndex_Type()
)
mtxrQueueTreeParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeParentIndex.setStatus("current")
_MtxrQueueTreeBytes_Type = Counter32
_MtxrQueueTreeBytes_Object = MibTableColumn
mtxrQueueTreeBytes = _MtxrQueueTreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 5),
    _MtxrQueueTreeBytes_Type()
)
mtxrQueueTreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeBytes.setStatus("current")
_MtxrQueueTreePackets_Type = Counter32
_MtxrQueueTreePackets_Object = MibTableColumn
mtxrQueueTreePackets = _MtxrQueueTreePackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 6),
    _MtxrQueueTreePackets_Type()
)
mtxrQueueTreePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreePackets.setStatus("current")
_MtxrQueueTreeHCBytes_Type = Counter64
_MtxrQueueTreeHCBytes_Object = MibTableColumn
mtxrQueueTreeHCBytes = _MtxrQueueTreeHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 7),
    _MtxrQueueTreeHCBytes_Type()
)
mtxrQueueTreeHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeHCBytes.setStatus("current")
_MtxrQueueTreePCQQueues_Type = Counter32
_MtxrQueueTreePCQQueues_Object = MibTableColumn
mtxrQueueTreePCQQueues = _MtxrQueueTreePCQQueues_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 8),
    _MtxrQueueTreePCQQueues_Type()
)
mtxrQueueTreePCQQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreePCQQueues.setStatus("current")
_MtxrQueueTreeDropped_Type = Counter32
_MtxrQueueTreeDropped_Object = MibTableColumn
mtxrQueueTreeDropped = _MtxrQueueTreeDropped_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 9),
    _MtxrQueueTreeDropped_Type()
)
mtxrQueueTreeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeDropped.setStatus("current")
_MtxrHealth_ObjectIdentity = ObjectIdentity
mtxrHealth = _MtxrHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3)
)
_MtxrHlCoreVoltage_Type = Voltage
_MtxrHlCoreVoltage_Object = MibScalar
mtxrHlCoreVoltage = _MtxrHlCoreVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 1),
    _MtxrHlCoreVoltage_Type()
)
mtxrHlCoreVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCoreVoltage.setStatus("current")
_MtxrHlThreeDotThreeVoltage_Type = Voltage
_MtxrHlThreeDotThreeVoltage_Object = MibScalar
mtxrHlThreeDotThreeVoltage = _MtxrHlThreeDotThreeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 2),
    _MtxrHlThreeDotThreeVoltage_Type()
)
mtxrHlThreeDotThreeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlThreeDotThreeVoltage.setStatus("current")
_MtxrHlFiveVoltage_Type = Voltage
_MtxrHlFiveVoltage_Object = MibScalar
mtxrHlFiveVoltage = _MtxrHlFiveVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 3),
    _MtxrHlFiveVoltage_Type()
)
mtxrHlFiveVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFiveVoltage.setStatus("current")
_MtxrHlTwelveVoltage_Type = Voltage
_MtxrHlTwelveVoltage_Object = MibScalar
mtxrHlTwelveVoltage = _MtxrHlTwelveVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 4),
    _MtxrHlTwelveVoltage_Type()
)
mtxrHlTwelveVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlTwelveVoltage.setStatus("current")
_MtxrHlSensorTemperature_Type = Temperature
_MtxrHlSensorTemperature_Object = MibScalar
mtxrHlSensorTemperature = _MtxrHlSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 5),
    _MtxrHlSensorTemperature_Type()
)
mtxrHlSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlSensorTemperature.setStatus("current")
_MtxrHlCpuTemperature_Type = Temperature
_MtxrHlCpuTemperature_Object = MibScalar
mtxrHlCpuTemperature = _MtxrHlCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 6),
    _MtxrHlCpuTemperature_Type()
)
mtxrHlCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCpuTemperature.setStatus("current")
_MtxrHlBoardTemperature_Type = Temperature
_MtxrHlBoardTemperature_Object = MibScalar
mtxrHlBoardTemperature = _MtxrHlBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 7),
    _MtxrHlBoardTemperature_Type()
)
mtxrHlBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlBoardTemperature.setStatus("current")
_MtxrHlVoltage_Type = Voltage
_MtxrHlVoltage_Object = MibScalar
mtxrHlVoltage = _MtxrHlVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 8),
    _MtxrHlVoltage_Type()
)
mtxrHlVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlVoltage.setStatus("current")
_MtxrHlActiveFan_Type = DisplayString
_MtxrHlActiveFan_Object = MibScalar
mtxrHlActiveFan = _MtxrHlActiveFan_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 9),
    _MtxrHlActiveFan_Type()
)
mtxrHlActiveFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlActiveFan.setStatus("current")
_MtxrHlTemperature_Type = Temperature
_MtxrHlTemperature_Object = MibScalar
mtxrHlTemperature = _MtxrHlTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 10),
    _MtxrHlTemperature_Type()
)
mtxrHlTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlTemperature.setStatus("current")
_MtxrHlProcessorTemperature_Type = Temperature
_MtxrHlProcessorTemperature_Object = MibScalar
mtxrHlProcessorTemperature = _MtxrHlProcessorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 11),
    _MtxrHlProcessorTemperature_Type()
)
mtxrHlProcessorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlProcessorTemperature.setStatus("current")
_MtxrHlPower_Type = Power
_MtxrHlPower_Object = MibScalar
mtxrHlPower = _MtxrHlPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 12),
    _MtxrHlPower_Type()
)
mtxrHlPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlPower.setStatus("current")
_MtxrHlCurrent_Type = Integer32
_MtxrHlCurrent_Object = MibScalar
mtxrHlCurrent = _MtxrHlCurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 13),
    _MtxrHlCurrent_Type()
)
mtxrHlCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCurrent.setStatus("current")
_MtxrHlProcessorFrequency_Type = Integer32
_MtxrHlProcessorFrequency_Object = MibScalar
mtxrHlProcessorFrequency = _MtxrHlProcessorFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 14),
    _MtxrHlProcessorFrequency_Type()
)
mtxrHlProcessorFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlProcessorFrequency.setStatus("current")
_MtxrHlPowerSupplyState_Type = BoolValue
_MtxrHlPowerSupplyState_Object = MibScalar
mtxrHlPowerSupplyState = _MtxrHlPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 15),
    _MtxrHlPowerSupplyState_Type()
)
mtxrHlPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlPowerSupplyState.setStatus("current")
_MtxrHlBackupPowerSupplyState_Type = BoolValue
_MtxrHlBackupPowerSupplyState_Object = MibScalar
mtxrHlBackupPowerSupplyState = _MtxrHlBackupPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 16),
    _MtxrHlBackupPowerSupplyState_Type()
)
mtxrHlBackupPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlBackupPowerSupplyState.setStatus("current")
_MtxrHlFanSpeed1_Type = Gauge32
_MtxrHlFanSpeed1_Object = MibScalar
mtxrHlFanSpeed1 = _MtxrHlFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 17),
    _MtxrHlFanSpeed1_Type()
)
mtxrHlFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFanSpeed1.setStatus("current")
_MtxrHlFanSpeed2_Type = Gauge32
_MtxrHlFanSpeed2_Object = MibScalar
mtxrHlFanSpeed2 = _MtxrHlFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 18),
    _MtxrHlFanSpeed2_Type()
)
mtxrHlFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFanSpeed2.setStatus("current")


class _MtxrAlarmSocketStatus_Type(Integer32):
    """Custom type mtxrAlarmSocketStatus based on Integer32"""
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


_MtxrAlarmSocketStatus_Type.__name__ = "Integer32"
_MtxrAlarmSocketStatus_Object = MibScalar
mtxrAlarmSocketStatus = _MtxrAlarmSocketStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 19),
    _MtxrAlarmSocketStatus_Type()
)
mtxrAlarmSocketStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrAlarmSocketStatus.setStatus("current")
_MtxrGaugeTable_Object = MibTable
mtxrGaugeTable = _MtxrGaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100)
)
if mibBuilder.loadTexts:
    mtxrGaugeTable.setStatus("current")
_MtxrGaugeTableEntry_Object = MibTableRow
mtxrGaugeTableEntry = _MtxrGaugeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100, 1)
)
mtxrGaugeTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrGaugeIndex"),
)
if mibBuilder.loadTexts:
    mtxrGaugeTableEntry.setStatus("current")
_MtxrGaugeIndex_Type = ObjectIndex
_MtxrGaugeIndex_Object = MibTableColumn
mtxrGaugeIndex = _MtxrGaugeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100, 1, 1),
    _MtxrGaugeIndex_Type()
)
mtxrGaugeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrGaugeIndex.setStatus("current")
_MtxrGaugeName_Type = DisplayString
_MtxrGaugeName_Object = MibTableColumn
mtxrGaugeName = _MtxrGaugeName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100, 1, 2),
    _MtxrGaugeName_Type()
)
mtxrGaugeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrGaugeName.setStatus("current")
_MtxrGaugeValue_Type = Integer32
_MtxrGaugeValue_Object = MibTableColumn
mtxrGaugeValue = _MtxrGaugeValue_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100, 1, 3),
    _MtxrGaugeValue_Type()
)
mtxrGaugeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrGaugeValue.setStatus("current")


class _MtxrGaugeUnit_Type(Integer32):
    """Custom type mtxrGaugeUnit based on Integer32"""
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
        *(("celsius", 1),
          ("rpm", 2),
          ("dV", 3),
          ("dA", 4),
          ("dW", 5),
          ("status", 6))
    )


_MtxrGaugeUnit_Type.__name__ = "Integer32"
_MtxrGaugeUnit_Object = MibTableColumn
mtxrGaugeUnit = _MtxrGaugeUnit_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 100, 1, 4),
    _MtxrGaugeUnit_Type()
)
mtxrGaugeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrGaugeUnit.setStatus("current")
_MtxrLicense_ObjectIdentity = ObjectIdentity
mtxrLicense = _MtxrLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4)
)
_MtxrLicSoftwareId_Type = DisplayString
_MtxrLicSoftwareId_Object = MibScalar
mtxrLicSoftwareId = _MtxrLicSoftwareId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 1),
    _MtxrLicSoftwareId_Type()
)
mtxrLicSoftwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicSoftwareId.setStatus("current")
_MtxrLicUpgrUntil_Type = DateAndTime
_MtxrLicUpgrUntil_Object = MibScalar
mtxrLicUpgrUntil = _MtxrLicUpgrUntil_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 2),
    _MtxrLicUpgrUntil_Type()
)
mtxrLicUpgrUntil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicUpgrUntil.setStatus("current")
_MtxrLicLevel_Type = Integer32
_MtxrLicLevel_Object = MibScalar
mtxrLicLevel = _MtxrLicLevel_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 3),
    _MtxrLicLevel_Type()
)
mtxrLicLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicLevel.setStatus("current")
_MtxrLicVersion_Type = DisplayString
_MtxrLicVersion_Object = MibScalar
mtxrLicVersion = _MtxrLicVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 4),
    _MtxrLicVersion_Type()
)
mtxrLicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicVersion.setStatus("current")
_MtxrLicUpgradableTo_Type = Integer32
_MtxrLicUpgradableTo_Object = MibScalar
mtxrLicUpgradableTo = _MtxrLicUpgradableTo_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 5),
    _MtxrLicUpgradableTo_Type()
)
mtxrLicUpgradableTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicUpgradableTo.setStatus("current")
_MtxrHotspot_ObjectIdentity = ObjectIdentity
mtxrHotspot = _MtxrHotspot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5)
)
_MtxrHotspotActiveUsersTable_Object = MibTable
mtxrHotspotActiveUsersTable = _MtxrHotspotActiveUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUsersTable.setStatus("current")
_MtxrHotspotActiveUsersTableEntry_Object = MibTableRow
mtxrHotspotActiveUsersTableEntry = _MtxrHotspotActiveUsersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1)
)
mtxrHotspotActiveUsersTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrHotspotActiveUserIndex"),
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUsersTableEntry.setStatus("current")
_MtxrHotspotActiveUserIndex_Type = ObjectIndex
_MtxrHotspotActiveUserIndex_Object = MibTableColumn
mtxrHotspotActiveUserIndex = _MtxrHotspotActiveUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 1),
    _MtxrHotspotActiveUserIndex_Type()
)
mtxrHotspotActiveUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIndex.setStatus("current")
_MtxrHotspotActiveUserServerID_Type = Integer32
_MtxrHotspotActiveUserServerID_Object = MibTableColumn
mtxrHotspotActiveUserServerID = _MtxrHotspotActiveUserServerID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 2),
    _MtxrHotspotActiveUserServerID_Type()
)
mtxrHotspotActiveUserServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserServerID.setStatus("current")
_MtxrHotspotActiveUserName_Type = DisplayString
_MtxrHotspotActiveUserName_Object = MibTableColumn
mtxrHotspotActiveUserName = _MtxrHotspotActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 3),
    _MtxrHotspotActiveUserName_Type()
)
mtxrHotspotActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserName.setStatus("current")
_MtxrHotspotActiveUserDomain_Type = DisplayString
_MtxrHotspotActiveUserDomain_Object = MibTableColumn
mtxrHotspotActiveUserDomain = _MtxrHotspotActiveUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 4),
    _MtxrHotspotActiveUserDomain_Type()
)
mtxrHotspotActiveUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserDomain.setStatus("current")
_MtxrHotspotActiveUserIP_Type = IpAddress
_MtxrHotspotActiveUserIP_Object = MibTableColumn
mtxrHotspotActiveUserIP = _MtxrHotspotActiveUserIP_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 5),
    _MtxrHotspotActiveUserIP_Type()
)
mtxrHotspotActiveUserIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIP.setStatus("current")
_MtxrHotspotActiveUserMAC_Type = MacAddress
_MtxrHotspotActiveUserMAC_Object = MibTableColumn
mtxrHotspotActiveUserMAC = _MtxrHotspotActiveUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 6),
    _MtxrHotspotActiveUserMAC_Type()
)
mtxrHotspotActiveUserMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserMAC.setStatus("current")
_MtxrHotspotActiveUserConnectTime_Type = Integer32
_MtxrHotspotActiveUserConnectTime_Object = MibTableColumn
mtxrHotspotActiveUserConnectTime = _MtxrHotspotActiveUserConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 7),
    _MtxrHotspotActiveUserConnectTime_Type()
)
mtxrHotspotActiveUserConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserConnectTime.setStatus("current")
_MtxrHotspotActiveUserValidTillTime_Type = Integer32
_MtxrHotspotActiveUserValidTillTime_Object = MibTableColumn
mtxrHotspotActiveUserValidTillTime = _MtxrHotspotActiveUserValidTillTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 8),
    _MtxrHotspotActiveUserValidTillTime_Type()
)
mtxrHotspotActiveUserValidTillTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserValidTillTime.setStatus("current")
_MtxrHotspotActiveUserIdleStartTime_Type = Integer32
_MtxrHotspotActiveUserIdleStartTime_Object = MibTableColumn
mtxrHotspotActiveUserIdleStartTime = _MtxrHotspotActiveUserIdleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 9),
    _MtxrHotspotActiveUserIdleStartTime_Type()
)
mtxrHotspotActiveUserIdleStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIdleStartTime.setStatus("current")
_MtxrHotspotActiveUserIdleTimeout_Type = Integer32
_MtxrHotspotActiveUserIdleTimeout_Object = MibTableColumn
mtxrHotspotActiveUserIdleTimeout = _MtxrHotspotActiveUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 10),
    _MtxrHotspotActiveUserIdleTimeout_Type()
)
mtxrHotspotActiveUserIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIdleTimeout.setStatus("current")
_MtxrHotspotActiveUserPingTimeout_Type = Integer32
_MtxrHotspotActiveUserPingTimeout_Object = MibTableColumn
mtxrHotspotActiveUserPingTimeout = _MtxrHotspotActiveUserPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 11),
    _MtxrHotspotActiveUserPingTimeout_Type()
)
mtxrHotspotActiveUserPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPingTimeout.setStatus("current")
_MtxrHotspotActiveUserBytesIn_Type = Counter64
_MtxrHotspotActiveUserBytesIn_Object = MibTableColumn
mtxrHotspotActiveUserBytesIn = _MtxrHotspotActiveUserBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 12),
    _MtxrHotspotActiveUserBytesIn_Type()
)
mtxrHotspotActiveUserBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBytesIn.setStatus("current")
_MtxrHotspotActiveUserBytesOut_Type = Counter64
_MtxrHotspotActiveUserBytesOut_Object = MibTableColumn
mtxrHotspotActiveUserBytesOut = _MtxrHotspotActiveUserBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 13),
    _MtxrHotspotActiveUserBytesOut_Type()
)
mtxrHotspotActiveUserBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBytesOut.setStatus("current")
_MtxrHotspotActiveUserPacketsIn_Type = Counter64
_MtxrHotspotActiveUserPacketsIn_Object = MibTableColumn
mtxrHotspotActiveUserPacketsIn = _MtxrHotspotActiveUserPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 14),
    _MtxrHotspotActiveUserPacketsIn_Type()
)
mtxrHotspotActiveUserPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPacketsIn.setStatus("current")
_MtxrHotspotActiveUserPacketsOut_Type = Counter64
_MtxrHotspotActiveUserPacketsOut_Object = MibTableColumn
mtxrHotspotActiveUserPacketsOut = _MtxrHotspotActiveUserPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 15),
    _MtxrHotspotActiveUserPacketsOut_Type()
)
mtxrHotspotActiveUserPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPacketsOut.setStatus("current")
_MtxrHotspotActiveUserLimitBytesIn_Type = Counter64
_MtxrHotspotActiveUserLimitBytesIn_Object = MibTableColumn
mtxrHotspotActiveUserLimitBytesIn = _MtxrHotspotActiveUserLimitBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 16),
    _MtxrHotspotActiveUserLimitBytesIn_Type()
)
mtxrHotspotActiveUserLimitBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserLimitBytesIn.setStatus("current")
_MtxrHotspotActiveUserLimitBytesOut_Type = Counter64
_MtxrHotspotActiveUserLimitBytesOut_Object = MibTableColumn
mtxrHotspotActiveUserLimitBytesOut = _MtxrHotspotActiveUserLimitBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 17),
    _MtxrHotspotActiveUserLimitBytesOut_Type()
)
mtxrHotspotActiveUserLimitBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserLimitBytesOut.setStatus("current")
_MtxrHotspotActiveUserAdvertStatus_Type = Integer32
_MtxrHotspotActiveUserAdvertStatus_Object = MibTableColumn
mtxrHotspotActiveUserAdvertStatus = _MtxrHotspotActiveUserAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 18),
    _MtxrHotspotActiveUserAdvertStatus_Type()
)
mtxrHotspotActiveUserAdvertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserAdvertStatus.setStatus("current")
_MtxrHotspotActiveUserRadius_Type = Integer32
_MtxrHotspotActiveUserRadius_Object = MibTableColumn
mtxrHotspotActiveUserRadius = _MtxrHotspotActiveUserRadius_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 19),
    _MtxrHotspotActiveUserRadius_Type()
)
mtxrHotspotActiveUserRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserRadius.setStatus("current")
_MtxrHotspotActiveUserBlockedByAdvert_Type = Integer32
_MtxrHotspotActiveUserBlockedByAdvert_Object = MibTableColumn
mtxrHotspotActiveUserBlockedByAdvert = _MtxrHotspotActiveUserBlockedByAdvert_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 20),
    _MtxrHotspotActiveUserBlockedByAdvert_Type()
)
mtxrHotspotActiveUserBlockedByAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBlockedByAdvert.setStatus("current")
_MtxrDHCP_ObjectIdentity = ObjectIdentity
mtxrDHCP = _MtxrDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 6)
)
_MtxrDHCPLeaseCount_Type = Gauge32
_MtxrDHCPLeaseCount_Object = MibScalar
mtxrDHCPLeaseCount = _MtxrDHCPLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 6, 1),
    _MtxrDHCPLeaseCount_Type()
)
mtxrDHCPLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDHCPLeaseCount.setStatus("current")
_MtxrSystem_ObjectIdentity = ObjectIdentity
mtxrSystem = _MtxrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7)
)
_MtxrSystemReboot_Type = Integer32
_MtxrSystemReboot_Object = MibScalar
mtxrSystemReboot = _MtxrSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 1),
    _MtxrSystemReboot_Type()
)
mtxrSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrSystemReboot.setStatus("current")
_MtxrUSBPowerReset_Type = Integer32
_MtxrUSBPowerReset_Object = MibScalar
mtxrUSBPowerReset = _MtxrUSBPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 2),
    _MtxrUSBPowerReset_Type()
)
mtxrUSBPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrUSBPowerReset.setStatus("current")
_MtxrSerialNumber_Type = DisplayString
_MtxrSerialNumber_Object = MibScalar
mtxrSerialNumber = _MtxrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 3),
    _MtxrSerialNumber_Type()
)
mtxrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSerialNumber.setStatus("current")
_MtxrFirmwareVersion_Type = DisplayString
_MtxrFirmwareVersion_Object = MibScalar
mtxrFirmwareVersion = _MtxrFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 4),
    _MtxrFirmwareVersion_Type()
)
mtxrFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrFirmwareVersion.setStatus("current")
_MtxrNote_Type = DisplayString
_MtxrNote_Object = MibScalar
mtxrNote = _MtxrNote_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 5),
    _MtxrNote_Type()
)
mtxrNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNote.setStatus("current")
_MtxrBuildTime_Type = DisplayString
_MtxrBuildTime_Object = MibScalar
mtxrBuildTime = _MtxrBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 6),
    _MtxrBuildTime_Type()
)
mtxrBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrBuildTime.setStatus("current")
_MtxrFirmwareUpgradeVersion_Type = DisplayString
_MtxrFirmwareUpgradeVersion_Object = MibScalar
mtxrFirmwareUpgradeVersion = _MtxrFirmwareUpgradeVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 7),
    _MtxrFirmwareUpgradeVersion_Type()
)
mtxrFirmwareUpgradeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrFirmwareUpgradeVersion.setStatus("current")
_MtxrDisplayName_Type = DisplayString
_MtxrDisplayName_Object = MibScalar
mtxrDisplayName = _MtxrDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 8),
    _MtxrDisplayName_Type()
)
mtxrDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDisplayName.setStatus("current")
_MtxrBoardName_Type = DisplayString
_MtxrBoardName_Object = MibScalar
mtxrBoardName = _MtxrBoardName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 9),
    _MtxrBoardName_Type()
)
mtxrBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrBoardName.setStatus("current")
_MtxrScripts_ObjectIdentity = ObjectIdentity
mtxrScripts = _MtxrScripts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8)
)
_MtxrScriptTable_Object = MibTable
mtxrScriptTable = _MtxrScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mtxrScriptTable.setStatus("current")
_MtxrScriptTableEntry_Object = MibTableRow
mtxrScriptTableEntry = _MtxrScriptTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1)
)
mtxrScriptTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrScriptIndex"),
)
if mibBuilder.loadTexts:
    mtxrScriptTableEntry.setStatus("current")
_MtxrScriptIndex_Type = ObjectIndex
_MtxrScriptIndex_Object = MibTableColumn
mtxrScriptIndex = _MtxrScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 1),
    _MtxrScriptIndex_Type()
)
mtxrScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrScriptIndex.setStatus("current")
_MtxrScriptName_Type = DisplayString
_MtxrScriptName_Object = MibTableColumn
mtxrScriptName = _MtxrScriptName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 2),
    _MtxrScriptName_Type()
)
mtxrScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrScriptName.setStatus("current")
_MtxrScriptRunCmd_Type = Integer32
_MtxrScriptRunCmd_Object = MibTableColumn
mtxrScriptRunCmd = _MtxrScriptRunCmd_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 3),
    _MtxrScriptRunCmd_Type()
)
mtxrScriptRunCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrScriptRunCmd.setStatus("current")
_MtxrTraps_ObjectIdentity = ObjectIdentity
mtxrTraps = _MtxrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9)
)
_MtxrNotifications_ObjectIdentity = ObjectIdentity
mtxrNotifications = _MtxrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0)
)
_MtxrNstremeDual_ObjectIdentity = ObjectIdentity
mtxrNstremeDual = _MtxrNstremeDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10)
)
_MtxrDnStatTable_Object = MibTable
mtxrDnStatTable = _MtxrDnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    mtxrDnStatTable.setStatus("current")
_MtxrDnStatEntry_Object = MibTableRow
mtxrDnStatEntry = _MtxrDnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1)
)
mtxrDnStatEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrDnStatIndex"),
)
if mibBuilder.loadTexts:
    mtxrDnStatEntry.setStatus("current")
_MtxrDnStatIndex_Type = ObjectIndex
_MtxrDnStatIndex_Object = MibTableColumn
mtxrDnStatIndex = _MtxrDnStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 1),
    _MtxrDnStatIndex_Type()
)
mtxrDnStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrDnStatIndex.setStatus("current")
_MtxrDnStatTxRate_Type = Gauge32
_MtxrDnStatTxRate_Object = MibTableColumn
mtxrDnStatTxRate = _MtxrDnStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 2),
    _MtxrDnStatTxRate_Type()
)
mtxrDnStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatTxRate.setStatus("current")
_MtxrDnStatRxRate_Type = Gauge32
_MtxrDnStatRxRate_Object = MibTableColumn
mtxrDnStatRxRate = _MtxrDnStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 3),
    _MtxrDnStatRxRate_Type()
)
mtxrDnStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatRxRate.setStatus("current")
_MtxrDnStatTxStrength_Type = Integer32
_MtxrDnStatTxStrength_Object = MibTableColumn
mtxrDnStatTxStrength = _MtxrDnStatTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 4),
    _MtxrDnStatTxStrength_Type()
)
mtxrDnStatTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatTxStrength.setStatus("current")
_MtxrDnStatRxStrength_Type = Integer32
_MtxrDnStatRxStrength_Object = MibTableColumn
mtxrDnStatRxStrength = _MtxrDnStatRxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 5),
    _MtxrDnStatRxStrength_Type()
)
mtxrDnStatRxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatRxStrength.setStatus("current")
_MtxrDnConnected_Type = Integer32
_MtxrDnConnected_Object = MibTableColumn
mtxrDnConnected = _MtxrDnConnected_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 6),
    _MtxrDnConnected_Type()
)
mtxrDnConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnConnected.setStatus("current")
_MtxrNeighbor_ObjectIdentity = ObjectIdentity
mtxrNeighbor = _MtxrNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11)
)
_MtxrNeighborTable_Object = MibTable
mtxrNeighborTable = _MtxrNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    mtxrNeighborTable.setStatus("current")
_MtxrNeighborTableEntry_Object = MibTableRow
mtxrNeighborTableEntry = _MtxrNeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1)
)
mtxrNeighborTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrNeighborIndex"),
)
if mibBuilder.loadTexts:
    mtxrNeighborTableEntry.setStatus("current")
_MtxrNeighborIndex_Type = ObjectIndex
_MtxrNeighborIndex_Object = MibTableColumn
mtxrNeighborIndex = _MtxrNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 1),
    _MtxrNeighborIndex_Type()
)
mtxrNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrNeighborIndex.setStatus("current")
_MtxrNeighborIpAddress_Type = IpAddress
_MtxrNeighborIpAddress_Object = MibTableColumn
mtxrNeighborIpAddress = _MtxrNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 2),
    _MtxrNeighborIpAddress_Type()
)
mtxrNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborIpAddress.setStatus("current")
_MtxrNeighborMacAddress_Type = MacAddress
_MtxrNeighborMacAddress_Object = MibTableColumn
mtxrNeighborMacAddress = _MtxrNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 3),
    _MtxrNeighborMacAddress_Type()
)
mtxrNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborMacAddress.setStatus("current")
_MtxrNeighborVersion_Type = DisplayString
_MtxrNeighborVersion_Object = MibTableColumn
mtxrNeighborVersion = _MtxrNeighborVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 4),
    _MtxrNeighborVersion_Type()
)
mtxrNeighborVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborVersion.setStatus("current")
_MtxrNeighborPlatform_Type = DisplayString
_MtxrNeighborPlatform_Object = MibTableColumn
mtxrNeighborPlatform = _MtxrNeighborPlatform_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 5),
    _MtxrNeighborPlatform_Type()
)
mtxrNeighborPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborPlatform.setStatus("current")
_MtxrNeighborIdentity_Type = DisplayString
_MtxrNeighborIdentity_Object = MibTableColumn
mtxrNeighborIdentity = _MtxrNeighborIdentity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 6),
    _MtxrNeighborIdentity_Type()
)
mtxrNeighborIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborIdentity.setStatus("current")
_MtxrNeighborSoftwareID_Type = DisplayString
_MtxrNeighborSoftwareID_Object = MibTableColumn
mtxrNeighborSoftwareID = _MtxrNeighborSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 7),
    _MtxrNeighborSoftwareID_Type()
)
mtxrNeighborSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborSoftwareID.setStatus("current")
_MtxrNeighborInterfaceID_Type = ObjectIndex
_MtxrNeighborInterfaceID_Object = MibTableColumn
mtxrNeighborInterfaceID = _MtxrNeighborInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 8),
    _MtxrNeighborInterfaceID_Type()
)
mtxrNeighborInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborInterfaceID.setStatus("current")
_MtxrGps_ObjectIdentity = ObjectIdentity
mtxrGps = _MtxrGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12)
)
_MtxrDate_Type = Integer32
_MtxrDate_Object = MibScalar
mtxrDate = _MtxrDate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 1),
    _MtxrDate_Type()
)
mtxrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDate.setStatus("current")
_MtxrLongtitude_Type = DisplayString
_MtxrLongtitude_Object = MibScalar
mtxrLongtitude = _MtxrLongtitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 2),
    _MtxrLongtitude_Type()
)
mtxrLongtitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLongtitude.setStatus("current")
_MtxrLatitude_Type = DisplayString
_MtxrLatitude_Object = MibScalar
mtxrLatitude = _MtxrLatitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 3),
    _MtxrLatitude_Type()
)
mtxrLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLatitude.setStatus("current")
_MtxrAltitude_Type = DisplayString
_MtxrAltitude_Object = MibScalar
mtxrAltitude = _MtxrAltitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 4),
    _MtxrAltitude_Type()
)
mtxrAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrAltitude.setStatus("current")
_MtxrSpeed_Type = DisplayString
_MtxrSpeed_Object = MibScalar
mtxrSpeed = _MtxrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 5),
    _MtxrSpeed_Type()
)
mtxrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSpeed.setStatus("current")
_MtxrSattelites_Type = Integer32
_MtxrSattelites_Object = MibScalar
mtxrSattelites = _MtxrSattelites_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 6),
    _MtxrSattelites_Type()
)
mtxrSattelites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSattelites.setStatus("current")
_MtxrValid_Type = Integer32
_MtxrValid_Object = MibScalar
mtxrValid = _MtxrValid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 7),
    _MtxrValid_Type()
)
mtxrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrValid.setStatus("current")
_MtxrWirelessModem_ObjectIdentity = ObjectIdentity
mtxrWirelessModem = _MtxrWirelessModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13)
)
_MtxrWirelessModemSignalStrength_Type = Integer32
_MtxrWirelessModemSignalStrength_Object = MibScalar
mtxrWirelessModemSignalStrength = _MtxrWirelessModemSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 1),
    _MtxrWirelessModemSignalStrength_Type()
)
mtxrWirelessModemSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemSignalStrength.setStatus("current")
_MtxrWirelessModemSignalECIO_Type = Integer32
_MtxrWirelessModemSignalECIO_Object = MibScalar
mtxrWirelessModemSignalECIO = _MtxrWirelessModemSignalECIO_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 2),
    _MtxrWirelessModemSignalECIO_Type()
)
mtxrWirelessModemSignalECIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemSignalECIO.setStatus("current")
_MtxrWirelessModemManufacturer_Type = DisplayString
_MtxrWirelessModemManufacturer_Object = MibScalar
mtxrWirelessModemManufacturer = _MtxrWirelessModemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 3),
    _MtxrWirelessModemManufacturer_Type()
)
mtxrWirelessModemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemManufacturer.setStatus("current")
_MtxrWirelessModemModel_Type = DisplayString
_MtxrWirelessModemModel_Object = MibScalar
mtxrWirelessModemModel = _MtxrWirelessModemModel_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 4),
    _MtxrWirelessModemModel_Type()
)
mtxrWirelessModemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemModel.setStatus("current")
_MtxrWirelessModemRevision_Type = DisplayString
_MtxrWirelessModemRevision_Object = MibScalar
mtxrWirelessModemRevision = _MtxrWirelessModemRevision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 5),
    _MtxrWirelessModemRevision_Type()
)
mtxrWirelessModemRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemRevision.setStatus("current")
_MtxrWirelessModemIMEI_Type = DisplayString
_MtxrWirelessModemIMEI_Object = MibScalar
mtxrWirelessModemIMEI = _MtxrWirelessModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 6),
    _MtxrWirelessModemIMEI_Type()
)
mtxrWirelessModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemIMEI.setStatus("current")
_MtxrWirelessModemIMSI_Type = DisplayString
_MtxrWirelessModemIMSI_Object = MibScalar
mtxrWirelessModemIMSI = _MtxrWirelessModemIMSI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 7),
    _MtxrWirelessModemIMSI_Type()
)
mtxrWirelessModemIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemIMSI.setStatus("current")
_MtxrWirelessModemAccessTechnology_Type = DisplayString
_MtxrWirelessModemAccessTechnology_Object = MibScalar
mtxrWirelessModemAccessTechnology = _MtxrWirelessModemAccessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 8),
    _MtxrWirelessModemAccessTechnology_Type()
)
mtxrWirelessModemAccessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemAccessTechnology.setStatus("current")
_MtxrWirelessModemFrameErrorRate_Type = DisplayString
_MtxrWirelessModemFrameErrorRate_Object = MibScalar
mtxrWirelessModemFrameErrorRate = _MtxrWirelessModemFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 9),
    _MtxrWirelessModemFrameErrorRate_Type()
)
mtxrWirelessModemFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemFrameErrorRate.setStatus("current")
_MtxrWirelessModemRSRP_Type = Integer32
_MtxrWirelessModemRSRP_Object = MibScalar
mtxrWirelessModemRSRP = _MtxrWirelessModemRSRP_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 10),
    _MtxrWirelessModemRSRP_Type()
)
mtxrWirelessModemRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemRSRP.setStatus("current")
_MtxrWirelessModemRSRQ_Type = Integer32
_MtxrWirelessModemRSRQ_Object = MibScalar
mtxrWirelessModemRSRQ = _MtxrWirelessModemRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 11),
    _MtxrWirelessModemRSRQ_Type()
)
mtxrWirelessModemRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemRSRQ.setStatus("current")
_MtxrWirelessModemSINR_Type = Integer32
_MtxrWirelessModemSINR_Object = MibScalar
mtxrWirelessModemSINR = _MtxrWirelessModemSINR_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 12),
    _MtxrWirelessModemSINR_Type()
)
mtxrWirelessModemSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemSINR.setStatus("current")
_MtxrWirelessModemPinStatus_Type = DisplayString
_MtxrWirelessModemPinStatus_Object = MibScalar
mtxrWirelessModemPinStatus = _MtxrWirelessModemPinStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 13),
    _MtxrWirelessModemPinStatus_Type()
)
mtxrWirelessModemPinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemPinStatus.setStatus("current")
_MtxrInterfaceStats_ObjectIdentity = ObjectIdentity
mtxrInterfaceStats = _MtxrInterfaceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14)
)
_MtxrInterfaceStatsTable_Object = MibTable
mtxrInterfaceStatsTable = _MtxrInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTable.setStatus("current")
_MtxrInterfaceStatsEntry_Object = MibTableRow
mtxrInterfaceStatsEntry = _MtxrInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1)
)
mtxrInterfaceStatsEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsEntry.setStatus("current")
_MtxrInterfaceStatsIndex_Type = ObjectIndex
_MtxrInterfaceStatsIndex_Object = MibTableColumn
mtxrInterfaceStatsIndex = _MtxrInterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 1),
    _MtxrInterfaceStatsIndex_Type()
)
mtxrInterfaceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsIndex.setStatus("current")
_MtxrInterfaceStatsName_Type = DisplayString
_MtxrInterfaceStatsName_Object = MibTableColumn
mtxrInterfaceStatsName = _MtxrInterfaceStatsName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 2),
    _MtxrInterfaceStatsName_Type()
)
mtxrInterfaceStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsName.setStatus("current")
_MtxrInterfaceStatsDriverRxBytes_Type = Counter64
_MtxrInterfaceStatsDriverRxBytes_Object = MibTableColumn
mtxrInterfaceStatsDriverRxBytes = _MtxrInterfaceStatsDriverRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 11),
    _MtxrInterfaceStatsDriverRxBytes_Type()
)
mtxrInterfaceStatsDriverRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverRxBytes.setStatus("current")
_MtxrInterfaceStatsDriverRxPackets_Type = Counter64
_MtxrInterfaceStatsDriverRxPackets_Object = MibTableColumn
mtxrInterfaceStatsDriverRxPackets = _MtxrInterfaceStatsDriverRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 12),
    _MtxrInterfaceStatsDriverRxPackets_Type()
)
mtxrInterfaceStatsDriverRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverRxPackets.setStatus("current")
_MtxrInterfaceStatsDriverTxBytes_Type = Counter64
_MtxrInterfaceStatsDriverTxBytes_Object = MibTableColumn
mtxrInterfaceStatsDriverTxBytes = _MtxrInterfaceStatsDriverTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 13),
    _MtxrInterfaceStatsDriverTxBytes_Type()
)
mtxrInterfaceStatsDriverTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverTxBytes.setStatus("current")
_MtxrInterfaceStatsDriverTxPackets_Type = Counter64
_MtxrInterfaceStatsDriverTxPackets_Object = MibTableColumn
mtxrInterfaceStatsDriverTxPackets = _MtxrInterfaceStatsDriverTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 14),
    _MtxrInterfaceStatsDriverTxPackets_Type()
)
mtxrInterfaceStatsDriverTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverTxPackets.setStatus("current")
_MtxrInterfaceStatsTxRx64_Type = Counter64
_MtxrInterfaceStatsTxRx64_Object = MibTableColumn
mtxrInterfaceStatsTxRx64 = _MtxrInterfaceStatsTxRx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 15),
    _MtxrInterfaceStatsTxRx64_Type()
)
mtxrInterfaceStatsTxRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx64.setStatus("current")
_MtxrInterfaceStatsTxRx65To127_Type = Counter64
_MtxrInterfaceStatsTxRx65To127_Object = MibTableColumn
mtxrInterfaceStatsTxRx65To127 = _MtxrInterfaceStatsTxRx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 16),
    _MtxrInterfaceStatsTxRx65To127_Type()
)
mtxrInterfaceStatsTxRx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx65To127.setStatus("current")
_MtxrInterfaceStatsTxRx128To255_Type = Counter64
_MtxrInterfaceStatsTxRx128To255_Object = MibTableColumn
mtxrInterfaceStatsTxRx128To255 = _MtxrInterfaceStatsTxRx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 17),
    _MtxrInterfaceStatsTxRx128To255_Type()
)
mtxrInterfaceStatsTxRx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx128To255.setStatus("current")
_MtxrInterfaceStatsTxRx256To511_Type = Counter64
_MtxrInterfaceStatsTxRx256To511_Object = MibTableColumn
mtxrInterfaceStatsTxRx256To511 = _MtxrInterfaceStatsTxRx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 18),
    _MtxrInterfaceStatsTxRx256To511_Type()
)
mtxrInterfaceStatsTxRx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx256To511.setStatus("current")
_MtxrInterfaceStatsTxRx512To1023_Type = Counter64
_MtxrInterfaceStatsTxRx512To1023_Object = MibTableColumn
mtxrInterfaceStatsTxRx512To1023 = _MtxrInterfaceStatsTxRx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 19),
    _MtxrInterfaceStatsTxRx512To1023_Type()
)
mtxrInterfaceStatsTxRx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx512To1023.setStatus("current")
_MtxrInterfaceStatsTxRx1024To1518_Type = Counter64
_MtxrInterfaceStatsTxRx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsTxRx1024To1518 = _MtxrInterfaceStatsTxRx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 20),
    _MtxrInterfaceStatsTxRx1024To1518_Type()
)
mtxrInterfaceStatsTxRx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx1024To1518.setStatus("current")
_MtxrInterfaceStatsTxRx1519ToMax_Type = Counter64
_MtxrInterfaceStatsTxRx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsTxRx1519ToMax = _MtxrInterfaceStatsTxRx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 21),
    _MtxrInterfaceStatsTxRx1519ToMax_Type()
)
mtxrInterfaceStatsTxRx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx1519ToMax.setStatus("current")
_MtxrInterfaceStatsRxBytes_Type = Counter64
_MtxrInterfaceStatsRxBytes_Object = MibTableColumn
mtxrInterfaceStatsRxBytes = _MtxrInterfaceStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 31),
    _MtxrInterfaceStatsRxBytes_Type()
)
mtxrInterfaceStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxBytes.setStatus("current")
_MtxrInterfaceStatsRxPackets_Type = Counter64
_MtxrInterfaceStatsRxPackets_Object = MibTableColumn
mtxrInterfaceStatsRxPackets = _MtxrInterfaceStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 32),
    _MtxrInterfaceStatsRxPackets_Type()
)
mtxrInterfaceStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxPackets.setStatus("current")
_MtxrInterfaceStatsRxTooShort_Type = Counter64
_MtxrInterfaceStatsRxTooShort_Object = MibTableColumn
mtxrInterfaceStatsRxTooShort = _MtxrInterfaceStatsRxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 33),
    _MtxrInterfaceStatsRxTooShort_Type()
)
mtxrInterfaceStatsRxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxTooShort.setStatus("current")
_MtxrInterfaceStatsRx64_Type = Counter64
_MtxrInterfaceStatsRx64_Object = MibTableColumn
mtxrInterfaceStatsRx64 = _MtxrInterfaceStatsRx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 34),
    _MtxrInterfaceStatsRx64_Type()
)
mtxrInterfaceStatsRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx64.setStatus("current")
_MtxrInterfaceStatsRx65To127_Type = Counter64
_MtxrInterfaceStatsRx65To127_Object = MibTableColumn
mtxrInterfaceStatsRx65To127 = _MtxrInterfaceStatsRx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 35),
    _MtxrInterfaceStatsRx65To127_Type()
)
mtxrInterfaceStatsRx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx65To127.setStatus("current")
_MtxrInterfaceStatsRx128To255_Type = Counter64
_MtxrInterfaceStatsRx128To255_Object = MibTableColumn
mtxrInterfaceStatsRx128To255 = _MtxrInterfaceStatsRx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 36),
    _MtxrInterfaceStatsRx128To255_Type()
)
mtxrInterfaceStatsRx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx128To255.setStatus("current")
_MtxrInterfaceStatsRx256To511_Type = Counter64
_MtxrInterfaceStatsRx256To511_Object = MibTableColumn
mtxrInterfaceStatsRx256To511 = _MtxrInterfaceStatsRx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 37),
    _MtxrInterfaceStatsRx256To511_Type()
)
mtxrInterfaceStatsRx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx256To511.setStatus("current")
_MtxrInterfaceStatsRx512To1023_Type = Counter64
_MtxrInterfaceStatsRx512To1023_Object = MibTableColumn
mtxrInterfaceStatsRx512To1023 = _MtxrInterfaceStatsRx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 38),
    _MtxrInterfaceStatsRx512To1023_Type()
)
mtxrInterfaceStatsRx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx512To1023.setStatus("current")
_MtxrInterfaceStatsRx1024To1518_Type = Counter64
_MtxrInterfaceStatsRx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsRx1024To1518 = _MtxrInterfaceStatsRx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 39),
    _MtxrInterfaceStatsRx1024To1518_Type()
)
mtxrInterfaceStatsRx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx1024To1518.setStatus("current")
_MtxrInterfaceStatsRx1519ToMax_Type = Counter64
_MtxrInterfaceStatsRx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsRx1519ToMax = _MtxrInterfaceStatsRx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 40),
    _MtxrInterfaceStatsRx1519ToMax_Type()
)
mtxrInterfaceStatsRx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx1519ToMax.setStatus("current")
_MtxrInterfaceStatsRxTooLong_Type = Counter64
_MtxrInterfaceStatsRxTooLong_Object = MibTableColumn
mtxrInterfaceStatsRxTooLong = _MtxrInterfaceStatsRxTooLong_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 41),
    _MtxrInterfaceStatsRxTooLong_Type()
)
mtxrInterfaceStatsRxTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxTooLong.setStatus("current")
_MtxrInterfaceStatsRxBroadcast_Type = Counter64
_MtxrInterfaceStatsRxBroadcast_Object = MibTableColumn
mtxrInterfaceStatsRxBroadcast = _MtxrInterfaceStatsRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 42),
    _MtxrInterfaceStatsRxBroadcast_Type()
)
mtxrInterfaceStatsRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxBroadcast.setStatus("current")
_MtxrInterfaceStatsRxPause_Type = Counter64
_MtxrInterfaceStatsRxPause_Object = MibTableColumn
mtxrInterfaceStatsRxPause = _MtxrInterfaceStatsRxPause_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 43),
    _MtxrInterfaceStatsRxPause_Type()
)
mtxrInterfaceStatsRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxPause.setStatus("current")
_MtxrInterfaceStatsRxMulticast_Type = Counter64
_MtxrInterfaceStatsRxMulticast_Object = MibTableColumn
mtxrInterfaceStatsRxMulticast = _MtxrInterfaceStatsRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 44),
    _MtxrInterfaceStatsRxMulticast_Type()
)
mtxrInterfaceStatsRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxMulticast.setStatus("current")
_MtxrInterfaceStatsRxFCSError_Type = Counter64
_MtxrInterfaceStatsRxFCSError_Object = MibTableColumn
mtxrInterfaceStatsRxFCSError = _MtxrInterfaceStatsRxFCSError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 45),
    _MtxrInterfaceStatsRxFCSError_Type()
)
mtxrInterfaceStatsRxFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxFCSError.setStatus("current")
_MtxrInterfaceStatsRxAlignError_Type = Counter64
_MtxrInterfaceStatsRxAlignError_Object = MibTableColumn
mtxrInterfaceStatsRxAlignError = _MtxrInterfaceStatsRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 46),
    _MtxrInterfaceStatsRxAlignError_Type()
)
mtxrInterfaceStatsRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxAlignError.setStatus("current")
_MtxrInterfaceStatsRxFragment_Type = Counter64
_MtxrInterfaceStatsRxFragment_Object = MibTableColumn
mtxrInterfaceStatsRxFragment = _MtxrInterfaceStatsRxFragment_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 47),
    _MtxrInterfaceStatsRxFragment_Type()
)
mtxrInterfaceStatsRxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxFragment.setStatus("current")
_MtxrInterfaceStatsRxOverflow_Type = Counter64
_MtxrInterfaceStatsRxOverflow_Object = MibTableColumn
mtxrInterfaceStatsRxOverflow = _MtxrInterfaceStatsRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 48),
    _MtxrInterfaceStatsRxOverflow_Type()
)
mtxrInterfaceStatsRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxOverflow.setStatus("current")
_MtxrInterfaceStatsRxControl_Type = Counter64
_MtxrInterfaceStatsRxControl_Object = MibTableColumn
mtxrInterfaceStatsRxControl = _MtxrInterfaceStatsRxControl_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 49),
    _MtxrInterfaceStatsRxControl_Type()
)
mtxrInterfaceStatsRxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxControl.setStatus("current")
_MtxrInterfaceStatsRxUnknownOp_Type = Counter64
_MtxrInterfaceStatsRxUnknownOp_Object = MibTableColumn
mtxrInterfaceStatsRxUnknownOp = _MtxrInterfaceStatsRxUnknownOp_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 50),
    _MtxrInterfaceStatsRxUnknownOp_Type()
)
mtxrInterfaceStatsRxUnknownOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxUnknownOp.setStatus("current")
_MtxrInterfaceStatsRxLengthError_Type = Counter64
_MtxrInterfaceStatsRxLengthError_Object = MibTableColumn
mtxrInterfaceStatsRxLengthError = _MtxrInterfaceStatsRxLengthError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 51),
    _MtxrInterfaceStatsRxLengthError_Type()
)
mtxrInterfaceStatsRxLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxLengthError.setStatus("current")
_MtxrInterfaceStatsRxCodeError_Type = Counter64
_MtxrInterfaceStatsRxCodeError_Object = MibTableColumn
mtxrInterfaceStatsRxCodeError = _MtxrInterfaceStatsRxCodeError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 52),
    _MtxrInterfaceStatsRxCodeError_Type()
)
mtxrInterfaceStatsRxCodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxCodeError.setStatus("current")
_MtxrInterfaceStatsRxCarrierError_Type = Counter64
_MtxrInterfaceStatsRxCarrierError_Object = MibTableColumn
mtxrInterfaceStatsRxCarrierError = _MtxrInterfaceStatsRxCarrierError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 53),
    _MtxrInterfaceStatsRxCarrierError_Type()
)
mtxrInterfaceStatsRxCarrierError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxCarrierError.setStatus("current")
_MtxrInterfaceStatsRxJabber_Type = Counter64
_MtxrInterfaceStatsRxJabber_Object = MibTableColumn
mtxrInterfaceStatsRxJabber = _MtxrInterfaceStatsRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 54),
    _MtxrInterfaceStatsRxJabber_Type()
)
mtxrInterfaceStatsRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxJabber.setStatus("current")
_MtxrInterfaceStatsRxDrop_Type = Counter64
_MtxrInterfaceStatsRxDrop_Object = MibTableColumn
mtxrInterfaceStatsRxDrop = _MtxrInterfaceStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 55),
    _MtxrInterfaceStatsRxDrop_Type()
)
mtxrInterfaceStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxDrop.setStatus("current")
_MtxrInterfaceStatsTxBytes_Type = Counter64
_MtxrInterfaceStatsTxBytes_Object = MibTableColumn
mtxrInterfaceStatsTxBytes = _MtxrInterfaceStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 61),
    _MtxrInterfaceStatsTxBytes_Type()
)
mtxrInterfaceStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxBytes.setStatus("current")
_MtxrInterfaceStatsTxPackets_Type = Counter64
_MtxrInterfaceStatsTxPackets_Object = MibTableColumn
mtxrInterfaceStatsTxPackets = _MtxrInterfaceStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 62),
    _MtxrInterfaceStatsTxPackets_Type()
)
mtxrInterfaceStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPackets.setStatus("current")
_MtxrInterfaceStatsTxTooShort_Type = Counter64
_MtxrInterfaceStatsTxTooShort_Object = MibTableColumn
mtxrInterfaceStatsTxTooShort = _MtxrInterfaceStatsTxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 63),
    _MtxrInterfaceStatsTxTooShort_Type()
)
mtxrInterfaceStatsTxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTooShort.setStatus("current")
_MtxrInterfaceStatsTx64_Type = Counter64
_MtxrInterfaceStatsTx64_Object = MibTableColumn
mtxrInterfaceStatsTx64 = _MtxrInterfaceStatsTx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 64),
    _MtxrInterfaceStatsTx64_Type()
)
mtxrInterfaceStatsTx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx64.setStatus("current")
_MtxrInterfaceStatsTx65To127_Type = Counter64
_MtxrInterfaceStatsTx65To127_Object = MibTableColumn
mtxrInterfaceStatsTx65To127 = _MtxrInterfaceStatsTx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 65),
    _MtxrInterfaceStatsTx65To127_Type()
)
mtxrInterfaceStatsTx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx65To127.setStatus("current")
_MtxrInterfaceStatsTx128To255_Type = Counter64
_MtxrInterfaceStatsTx128To255_Object = MibTableColumn
mtxrInterfaceStatsTx128To255 = _MtxrInterfaceStatsTx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 66),
    _MtxrInterfaceStatsTx128To255_Type()
)
mtxrInterfaceStatsTx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx128To255.setStatus("current")
_MtxrInterfaceStatsTx256To511_Type = Counter64
_MtxrInterfaceStatsTx256To511_Object = MibTableColumn
mtxrInterfaceStatsTx256To511 = _MtxrInterfaceStatsTx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 67),
    _MtxrInterfaceStatsTx256To511_Type()
)
mtxrInterfaceStatsTx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx256To511.setStatus("current")
_MtxrInterfaceStatsTx512To1023_Type = Counter64
_MtxrInterfaceStatsTx512To1023_Object = MibTableColumn
mtxrInterfaceStatsTx512To1023 = _MtxrInterfaceStatsTx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 68),
    _MtxrInterfaceStatsTx512To1023_Type()
)
mtxrInterfaceStatsTx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx512To1023.setStatus("current")
_MtxrInterfaceStatsTx1024To1518_Type = Counter64
_MtxrInterfaceStatsTx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsTx1024To1518 = _MtxrInterfaceStatsTx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 69),
    _MtxrInterfaceStatsTx1024To1518_Type()
)
mtxrInterfaceStatsTx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx1024To1518.setStatus("current")
_MtxrInterfaceStatsTx1519ToMax_Type = Counter64
_MtxrInterfaceStatsTx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsTx1519ToMax = _MtxrInterfaceStatsTx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 70),
    _MtxrInterfaceStatsTx1519ToMax_Type()
)
mtxrInterfaceStatsTx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx1519ToMax.setStatus("current")
_MtxrInterfaceStatsTxTooLong_Type = Counter64
_MtxrInterfaceStatsTxTooLong_Object = MibTableColumn
mtxrInterfaceStatsTxTooLong = _MtxrInterfaceStatsTxTooLong_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 71),
    _MtxrInterfaceStatsTxTooLong_Type()
)
mtxrInterfaceStatsTxTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTooLong.setStatus("current")
_MtxrInterfaceStatsTxBroadcast_Type = Counter64
_MtxrInterfaceStatsTxBroadcast_Object = MibTableColumn
mtxrInterfaceStatsTxBroadcast = _MtxrInterfaceStatsTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 72),
    _MtxrInterfaceStatsTxBroadcast_Type()
)
mtxrInterfaceStatsTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxBroadcast.setStatus("current")
_MtxrInterfaceStatsTxPause_Type = Counter64
_MtxrInterfaceStatsTxPause_Object = MibTableColumn
mtxrInterfaceStatsTxPause = _MtxrInterfaceStatsTxPause_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 73),
    _MtxrInterfaceStatsTxPause_Type()
)
mtxrInterfaceStatsTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPause.setStatus("current")
_MtxrInterfaceStatsTxMulticast_Type = Counter64
_MtxrInterfaceStatsTxMulticast_Object = MibTableColumn
mtxrInterfaceStatsTxMulticast = _MtxrInterfaceStatsTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 74),
    _MtxrInterfaceStatsTxMulticast_Type()
)
mtxrInterfaceStatsTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxMulticast.setStatus("current")
_MtxrInterfaceStatsTxUnderrun_Type = Counter64
_MtxrInterfaceStatsTxUnderrun_Object = MibTableColumn
mtxrInterfaceStatsTxUnderrun = _MtxrInterfaceStatsTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 75),
    _MtxrInterfaceStatsTxUnderrun_Type()
)
mtxrInterfaceStatsTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxUnderrun.setStatus("current")
_MtxrInterfaceStatsTxCollision_Type = Counter64
_MtxrInterfaceStatsTxCollision_Object = MibTableColumn
mtxrInterfaceStatsTxCollision = _MtxrInterfaceStatsTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 76),
    _MtxrInterfaceStatsTxCollision_Type()
)
mtxrInterfaceStatsTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxCollision.setStatus("current")
_MtxrInterfaceStatsTxExcessiveCollision_Type = Counter64
_MtxrInterfaceStatsTxExcessiveCollision_Object = MibTableColumn
mtxrInterfaceStatsTxExcessiveCollision = _MtxrInterfaceStatsTxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 77),
    _MtxrInterfaceStatsTxExcessiveCollision_Type()
)
mtxrInterfaceStatsTxExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxExcessiveCollision.setStatus("current")
_MtxrInterfaceStatsTxMultipleCollision_Type = Counter64
_MtxrInterfaceStatsTxMultipleCollision_Object = MibTableColumn
mtxrInterfaceStatsTxMultipleCollision = _MtxrInterfaceStatsTxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 78),
    _MtxrInterfaceStatsTxMultipleCollision_Type()
)
mtxrInterfaceStatsTxMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxMultipleCollision.setStatus("current")
_MtxrInterfaceStatsTxSingleCollision_Type = Counter64
_MtxrInterfaceStatsTxSingleCollision_Object = MibTableColumn
mtxrInterfaceStatsTxSingleCollision = _MtxrInterfaceStatsTxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 79),
    _MtxrInterfaceStatsTxSingleCollision_Type()
)
mtxrInterfaceStatsTxSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxSingleCollision.setStatus("current")
_MtxrInterfaceStatsTxExcessiveDeferred_Type = Counter64
_MtxrInterfaceStatsTxExcessiveDeferred_Object = MibTableColumn
mtxrInterfaceStatsTxExcessiveDeferred = _MtxrInterfaceStatsTxExcessiveDeferred_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 80),
    _MtxrInterfaceStatsTxExcessiveDeferred_Type()
)
mtxrInterfaceStatsTxExcessiveDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxExcessiveDeferred.setStatus("current")
_MtxrInterfaceStatsTxDeferred_Type = Counter64
_MtxrInterfaceStatsTxDeferred_Object = MibTableColumn
mtxrInterfaceStatsTxDeferred = _MtxrInterfaceStatsTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 81),
    _MtxrInterfaceStatsTxDeferred_Type()
)
mtxrInterfaceStatsTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxDeferred.setStatus("current")
_MtxrInterfaceStatsTxLateCollision_Type = Counter64
_MtxrInterfaceStatsTxLateCollision_Object = MibTableColumn
mtxrInterfaceStatsTxLateCollision = _MtxrInterfaceStatsTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 82),
    _MtxrInterfaceStatsTxLateCollision_Type()
)
mtxrInterfaceStatsTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxLateCollision.setStatus("current")
_MtxrInterfaceStatsTxTotalCollision_Type = Counter64
_MtxrInterfaceStatsTxTotalCollision_Object = MibTableColumn
mtxrInterfaceStatsTxTotalCollision = _MtxrInterfaceStatsTxTotalCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 83),
    _MtxrInterfaceStatsTxTotalCollision_Type()
)
mtxrInterfaceStatsTxTotalCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTotalCollision.setStatus("current")
_MtxrInterfaceStatsTxPauseHonored_Type = Counter64
_MtxrInterfaceStatsTxPauseHonored_Object = MibTableColumn
mtxrInterfaceStatsTxPauseHonored = _MtxrInterfaceStatsTxPauseHonored_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 84),
    _MtxrInterfaceStatsTxPauseHonored_Type()
)
mtxrInterfaceStatsTxPauseHonored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPauseHonored.setStatus("current")
_MtxrInterfaceStatsTxDrop_Type = Counter64
_MtxrInterfaceStatsTxDrop_Object = MibTableColumn
mtxrInterfaceStatsTxDrop = _MtxrInterfaceStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 85),
    _MtxrInterfaceStatsTxDrop_Type()
)
mtxrInterfaceStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxDrop.setStatus("current")
_MtxrInterfaceStatsTxJabber_Type = Counter64
_MtxrInterfaceStatsTxJabber_Object = MibTableColumn
mtxrInterfaceStatsTxJabber = _MtxrInterfaceStatsTxJabber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 86),
    _MtxrInterfaceStatsTxJabber_Type()
)
mtxrInterfaceStatsTxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxJabber.setStatus("current")
_MtxrInterfaceStatsTxFCSError_Type = Counter64
_MtxrInterfaceStatsTxFCSError_Object = MibTableColumn
mtxrInterfaceStatsTxFCSError = _MtxrInterfaceStatsTxFCSError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 87),
    _MtxrInterfaceStatsTxFCSError_Type()
)
mtxrInterfaceStatsTxFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxFCSError.setStatus("current")
_MtxrInterfaceStatsTxControl_Type = Counter64
_MtxrInterfaceStatsTxControl_Object = MibTableColumn
mtxrInterfaceStatsTxControl = _MtxrInterfaceStatsTxControl_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 88),
    _MtxrInterfaceStatsTxControl_Type()
)
mtxrInterfaceStatsTxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxControl.setStatus("current")
_MtxrInterfaceStatsTxFragment_Type = Counter64
_MtxrInterfaceStatsTxFragment_Object = MibTableColumn
mtxrInterfaceStatsTxFragment = _MtxrInterfaceStatsTxFragment_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 89),
    _MtxrInterfaceStatsTxFragment_Type()
)
mtxrInterfaceStatsTxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxFragment.setStatus("current")
_MtxrInterfaceStatsLinkDowns_Type = Counter32
_MtxrInterfaceStatsLinkDowns_Object = MibTableColumn
mtxrInterfaceStatsLinkDowns = _MtxrInterfaceStatsLinkDowns_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 90),
    _MtxrInterfaceStatsLinkDowns_Type()
)
mtxrInterfaceStatsLinkDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsLinkDowns.setStatus("current")
_MtxrInterfaceStatsTxRx1024ToMax_Type = Counter64
_MtxrInterfaceStatsTxRx1024ToMax_Object = MibTableColumn
mtxrInterfaceStatsTxRx1024ToMax = _MtxrInterfaceStatsTxRx1024ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 91),
    _MtxrInterfaceStatsTxRx1024ToMax_Type()
)
mtxrInterfaceStatsTxRx1024ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx1024ToMax.setStatus("current")
_MtxrPOE_ObjectIdentity = ObjectIdentity
mtxrPOE = _MtxrPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15)
)
_MtxrPOETable_Object = MibTable
mtxrPOETable = _MtxrPOETable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    mtxrPOETable.setStatus("current")
_MtxrPOEEntry_Object = MibTableRow
mtxrPOEEntry = _MtxrPOEEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1)
)
mtxrPOEEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrPOEInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mtxrPOEEntry.setStatus("current")
_MtxrPOEInterfaceIndex_Type = ObjectIndex
_MtxrPOEInterfaceIndex_Object = MibTableColumn
mtxrPOEInterfaceIndex = _MtxrPOEInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 1),
    _MtxrPOEInterfaceIndex_Type()
)
mtxrPOEInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrPOEInterfaceIndex.setStatus("current")
_MtxrPOEName_Type = DisplayString
_MtxrPOEName_Object = MibTableColumn
mtxrPOEName = _MtxrPOEName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 2),
    _MtxrPOEName_Type()
)
mtxrPOEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEName.setStatus("current")


class _MtxrPOEStatus_Type(Integer32):
    """Custom type mtxrPOEStatus based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("waitingForLoad", 2),
          ("poweredOn", 3),
          ("overload", 4),
          ("shortCircuit", 5),
          ("voltageTooLow", 6),
          ("currentTooLow", 7),
          ("powerReset", 8),
          ("voltageTooHigh", 9),
          ("controllerError", 10),
          ("controllerUpgrade", 11),
          ("poeInDetected", 12),
          ("noValidPsu", 13),
          ("controllerInit", 14),
          ("lowVoltageTooLow", 15))
    )


_MtxrPOEStatus_Type.__name__ = "Integer32"
_MtxrPOEStatus_Object = MibTableColumn
mtxrPOEStatus = _MtxrPOEStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 3),
    _MtxrPOEStatus_Type()
)
mtxrPOEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEStatus.setStatus("current")
_MtxrPOEVoltage_Type = Voltage
_MtxrPOEVoltage_Object = MibTableColumn
mtxrPOEVoltage = _MtxrPOEVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 4),
    _MtxrPOEVoltage_Type()
)
mtxrPOEVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEVoltage.setStatus("current")
_MtxrPOECurrent_Type = Integer32
_MtxrPOECurrent_Object = MibTableColumn
mtxrPOECurrent = _MtxrPOECurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 5),
    _MtxrPOECurrent_Type()
)
mtxrPOECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOECurrent.setStatus("current")
_MtxrPOEPower_Type = Power
_MtxrPOEPower_Object = MibTableColumn
mtxrPOEPower = _MtxrPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 6),
    _MtxrPOEPower_Type()
)
mtxrPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEPower.setStatus("current")
_MtxrLTEModem_ObjectIdentity = ObjectIdentity
mtxrLTEModem = _MtxrLTEModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16)
)
_MtxrLTEModemTable_Object = MibTable
mtxrLTEModemTable = _MtxrLTEModemTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    mtxrLTEModemTable.setStatus("current")
_MtxrLTEModemEntry_Object = MibTableRow
mtxrLTEModemEntry = _MtxrLTEModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1)
)
mtxrLTEModemEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrLTEModemInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mtxrLTEModemEntry.setStatus("current")
_MtxrLTEModemInterfaceIndex_Type = ObjectIndex
_MtxrLTEModemInterfaceIndex_Object = MibTableColumn
mtxrLTEModemInterfaceIndex = _MtxrLTEModemInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 1),
    _MtxrLTEModemInterfaceIndex_Type()
)
mtxrLTEModemInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrLTEModemInterfaceIndex.setStatus("current")
_MtxrLTEModemSignalRSSI_Type = Integer32
_MtxrLTEModemSignalRSSI_Object = MibTableColumn
mtxrLTEModemSignalRSSI = _MtxrLTEModemSignalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 2),
    _MtxrLTEModemSignalRSSI_Type()
)
mtxrLTEModemSignalRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSSI.setStatus("current")
_MtxrLTEModemSignalRSRQ_Type = Integer32
_MtxrLTEModemSignalRSRQ_Object = MibTableColumn
mtxrLTEModemSignalRSRQ = _MtxrLTEModemSignalRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 3),
    _MtxrLTEModemSignalRSRQ_Type()
)
mtxrLTEModemSignalRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSRQ.setStatus("current")
_MtxrLTEModemSignalRSRP_Type = Integer32
_MtxrLTEModemSignalRSRP_Object = MibTableColumn
mtxrLTEModemSignalRSRP = _MtxrLTEModemSignalRSRP_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 4),
    _MtxrLTEModemSignalRSRP_Type()
)
mtxrLTEModemSignalRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSRP.setStatus("current")
_MtxrLTEModemCellId_Type = HexInt
_MtxrLTEModemCellId_Object = MibTableColumn
mtxrLTEModemCellId = _MtxrLTEModemCellId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 5),
    _MtxrLTEModemCellId_Type()
)
mtxrLTEModemCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemCellId.setStatus("current")


class _MtxrLTEModemAccessTechnology_Type(Integer32):
    """Custom type mtxrLTEModemAccessTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("gsmcompact", 0),
          ("gsm", 1),
          ("utran", 2),
          ("egprs", 3),
          ("hsdpa", 4),
          ("hsupa", 5),
          ("hsdpahsupa", 6),
          ("eutran", 7),
          ("nr-sa", 11),
          ("nr-nsa", 13))
    )


_MtxrLTEModemAccessTechnology_Type.__name__ = "Integer32"
_MtxrLTEModemAccessTechnology_Object = MibTableColumn
mtxrLTEModemAccessTechnology = _MtxrLTEModemAccessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 6),
    _MtxrLTEModemAccessTechnology_Type()
)
mtxrLTEModemAccessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemAccessTechnology.setStatus("current")
_MtxrLTEModemSignalSINR_Type = Integer32
_MtxrLTEModemSignalSINR_Object = MibTableColumn
mtxrLTEModemSignalSINR = _MtxrLTEModemSignalSINR_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 7),
    _MtxrLTEModemSignalSINR_Type()
)
mtxrLTEModemSignalSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalSINR.setStatus("current")
_MtxrLTEModemEnbId_Type = Integer32
_MtxrLTEModemEnbId_Object = MibTableColumn
mtxrLTEModemEnbId = _MtxrLTEModemEnbId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 8),
    _MtxrLTEModemEnbId_Type()
)
mtxrLTEModemEnbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemEnbId.setStatus("current")
_MtxrLTEModemSectorId_Type = Integer32
_MtxrLTEModemSectorId_Object = MibTableColumn
mtxrLTEModemSectorId = _MtxrLTEModemSectorId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 9),
    _MtxrLTEModemSectorId_Type()
)
mtxrLTEModemSectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSectorId.setStatus("current")
_MtxrLTEModemLac_Type = Integer32
_MtxrLTEModemLac_Object = MibTableColumn
mtxrLTEModemLac = _MtxrLTEModemLac_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 10),
    _MtxrLTEModemLac_Type()
)
mtxrLTEModemLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemLac.setStatus("current")
_MtxrLTEModemIMEI_Type = DisplayString
_MtxrLTEModemIMEI_Object = MibTableColumn
mtxrLTEModemIMEI = _MtxrLTEModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 11),
    _MtxrLTEModemIMEI_Type()
)
mtxrLTEModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemIMEI.setStatus("current")
_MtxrLTEModemIMSI_Type = DisplayString
_MtxrLTEModemIMSI_Object = MibTableColumn
mtxrLTEModemIMSI = _MtxrLTEModemIMSI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 12),
    _MtxrLTEModemIMSI_Type()
)
mtxrLTEModemIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemIMSI.setStatus("current")
_MtxrLTEModemUICC_Type = DisplayString
_MtxrLTEModemUICC_Object = MibTableColumn
mtxrLTEModemUICC = _MtxrLTEModemUICC_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 13),
    _MtxrLTEModemUICC_Type()
)
mtxrLTEModemUICC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemUICC.setStatus("current")
_MtxrLTEModemRAT_Type = DisplayString
_MtxrLTEModemRAT_Object = MibTableColumn
mtxrLTEModemRAT = _MtxrLTEModemRAT_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 14),
    _MtxrLTEModemRAT_Type()
)
mtxrLTEModemRAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemRAT.setStatus("current")
_MtxrPartition_ObjectIdentity = ObjectIdentity
mtxrPartition = _MtxrPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17)
)
_MtxrPartitionTable_Object = MibTable
mtxrPartitionTable = _MtxrPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    mtxrPartitionTable.setStatus("current")
_MtxrPartitionEntry_Object = MibTableRow
mtxrPartitionEntry = _MtxrPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1)
)
mtxrPartitionEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrPartitionIndex"),
)
if mibBuilder.loadTexts:
    mtxrPartitionEntry.setStatus("current")
_MtxrPartitionIndex_Type = ObjectIndex
_MtxrPartitionIndex_Object = MibTableColumn
mtxrPartitionIndex = _MtxrPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 1),
    _MtxrPartitionIndex_Type()
)
mtxrPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrPartitionIndex.setStatus("current")
_MtxrPartitionName_Type = DisplayString
_MtxrPartitionName_Object = MibTableColumn
mtxrPartitionName = _MtxrPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 2),
    _MtxrPartitionName_Type()
)
mtxrPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionName.setStatus("current")
_MtxrPartitionSize_Type = Integer32
_MtxrPartitionSize_Object = MibTableColumn
mtxrPartitionSize = _MtxrPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 3),
    _MtxrPartitionSize_Type()
)
mtxrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionSize.setStatus("current")
_MtxrPartitionVersion_Type = DisplayString
_MtxrPartitionVersion_Object = MibTableColumn
mtxrPartitionVersion = _MtxrPartitionVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 4),
    _MtxrPartitionVersion_Type()
)
mtxrPartitionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionVersion.setStatus("current")
_MtxrPartitionActive_Type = BoolValue
_MtxrPartitionActive_Object = MibTableColumn
mtxrPartitionActive = _MtxrPartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 5),
    _MtxrPartitionActive_Type()
)
mtxrPartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionActive.setStatus("current")
_MtxrPartitionRunning_Type = BoolValue
_MtxrPartitionRunning_Object = MibTableColumn
mtxrPartitionRunning = _MtxrPartitionRunning_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 6),
    _MtxrPartitionRunning_Type()
)
mtxrPartitionRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionRunning.setStatus("current")
_MtxrScriptRun_ObjectIdentity = ObjectIdentity
mtxrScriptRun = _MtxrScriptRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18)
)
_MtxrScriptRunTable_Object = MibTable
mtxrScriptRunTable = _MtxrScriptRunTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    mtxrScriptRunTable.setStatus("current")
_MtxrScriptRunTableEntry_Object = MibTableRow
mtxrScriptRunTableEntry = _MtxrScriptRunTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1)
)
mtxrScriptRunTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrScriptRunIndex"),
)
if mibBuilder.loadTexts:
    mtxrScriptRunTableEntry.setStatus("current")
_MtxrScriptRunIndex_Type = ObjectIndex
_MtxrScriptRunIndex_Object = MibTableColumn
mtxrScriptRunIndex = _MtxrScriptRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1, 1),
    _MtxrScriptRunIndex_Type()
)
mtxrScriptRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrScriptRunIndex.setStatus("current")
_MtxrScriptRunOutput_Type = DisplayString
_MtxrScriptRunOutput_Object = MibTableColumn
mtxrScriptRunOutput = _MtxrScriptRunOutput_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1, 2),
    _MtxrScriptRunOutput_Type()
)
mtxrScriptRunOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrScriptRunOutput.setStatus("current")
_MtxrOptical_ObjectIdentity = ObjectIdentity
mtxrOptical = _MtxrOptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19)
)
_MtxrOpticalTable_Object = MibTable
mtxrOpticalTable = _MtxrOpticalTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    mtxrOpticalTable.setStatus("current")
_MtxrOpticalTableEntry_Object = MibTableRow
mtxrOpticalTableEntry = _MtxrOpticalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1)
)
mtxrOpticalTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrOpticalIndex"),
)
if mibBuilder.loadTexts:
    mtxrOpticalTableEntry.setStatus("current")
_MtxrOpticalIndex_Type = ObjectIndex
_MtxrOpticalIndex_Object = MibTableColumn
mtxrOpticalIndex = _MtxrOpticalIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 1),
    _MtxrOpticalIndex_Type()
)
mtxrOpticalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrOpticalIndex.setStatus("current")
_MtxrOpticalName_Type = DisplayString
_MtxrOpticalName_Object = MibTableColumn
mtxrOpticalName = _MtxrOpticalName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 2),
    _MtxrOpticalName_Type()
)
mtxrOpticalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalName.setStatus("current")
_MtxrOpticalRxLoss_Type = BoolValue
_MtxrOpticalRxLoss_Object = MibTableColumn
mtxrOpticalRxLoss = _MtxrOpticalRxLoss_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 3),
    _MtxrOpticalRxLoss_Type()
)
mtxrOpticalRxLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalRxLoss.setStatus("current")
_MtxrOpticalTxFault_Type = BoolValue
_MtxrOpticalTxFault_Object = MibTableColumn
mtxrOpticalTxFault = _MtxrOpticalTxFault_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 4),
    _MtxrOpticalTxFault_Type()
)
mtxrOpticalTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxFault.setStatus("current")
_MtxrOpticalWavelength_Type = GDiv100
_MtxrOpticalWavelength_Object = MibTableColumn
mtxrOpticalWavelength = _MtxrOpticalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 5),
    _MtxrOpticalWavelength_Type()
)
mtxrOpticalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalWavelength.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalWavelength.setUnits("nm")
_MtxrOpticalTemperature_Type = Gauge32
_MtxrOpticalTemperature_Object = MibTableColumn
mtxrOpticalTemperature = _MtxrOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 6),
    _MtxrOpticalTemperature_Type()
)
mtxrOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTemperature.setUnits("C")
_MtxrOpticalSupplyVoltage_Type = GDiv1000
_MtxrOpticalSupplyVoltage_Object = MibTableColumn
mtxrOpticalSupplyVoltage = _MtxrOpticalSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 7),
    _MtxrOpticalSupplyVoltage_Type()
)
mtxrOpticalSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalSupplyVoltage.setUnits("V")
_MtxrOpticalTxBiasCurrent_Type = Gauge32
_MtxrOpticalTxBiasCurrent_Object = MibTableColumn
mtxrOpticalTxBiasCurrent = _MtxrOpticalTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 8),
    _MtxrOpticalTxBiasCurrent_Type()
)
mtxrOpticalTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTxBiasCurrent.setUnits("mA")
_MtxrOpticalTxPower_Type = IDiv1000
_MtxrOpticalTxPower_Object = MibTableColumn
mtxrOpticalTxPower = _MtxrOpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 9),
    _MtxrOpticalTxPower_Type()
)
mtxrOpticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTxPower.setUnits("dBm")
_MtxrOpticalRxPower_Type = IDiv1000
_MtxrOpticalRxPower_Object = MibTableColumn
mtxrOpticalRxPower = _MtxrOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 10),
    _MtxrOpticalRxPower_Type()
)
mtxrOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalRxPower.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalRxPower.setUnits("dBm")
_MtxrOpticalVendorName_Type = DisplayString
_MtxrOpticalVendorName_Object = MibTableColumn
mtxrOpticalVendorName = _MtxrOpticalVendorName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 11),
    _MtxrOpticalVendorName_Type()
)
mtxrOpticalVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalVendorName.setStatus("current")
_MtxrOpticalVendorSerial_Type = DisplayString
_MtxrOpticalVendorSerial_Object = MibTableColumn
mtxrOpticalVendorSerial = _MtxrOpticalVendorSerial_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 12),
    _MtxrOpticalVendorSerial_Type()
)
mtxrOpticalVendorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalVendorSerial.setStatus("current")
_MtxrIPSec_ObjectIdentity = ObjectIdentity
mtxrIPSec = _MtxrIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20)
)
_MtxrIkeSACount_Type = Gauge32
_MtxrIkeSACount_Object = MibScalar
mtxrIkeSACount = _MtxrIkeSACount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 1),
    _MtxrIkeSACount_Type()
)
mtxrIkeSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSACount.setStatus("current")
_MtxrIkeSATable_Object = MibTable
mtxrIkeSATable = _MtxrIkeSATable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    mtxrIkeSATable.setStatus("current")
_MtxrIkeSATableEntry_Object = MibTableRow
mtxrIkeSATableEntry = _MtxrIkeSATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1)
)
mtxrIkeSATableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrIkeSAIndex"),
)
if mibBuilder.loadTexts:
    mtxrIkeSATableEntry.setStatus("current")
_MtxrIkeSAIndex_Type = ObjectIndex
_MtxrIkeSAIndex_Object = MibTableColumn
mtxrIkeSAIndex = _MtxrIkeSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 1),
    _MtxrIkeSAIndex_Type()
)
mtxrIkeSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrIkeSAIndex.setStatus("current")
_MtxrIkeSAInitiatorCookie_Type = IsakmpCookie
_MtxrIkeSAInitiatorCookie_Object = MibTableColumn
mtxrIkeSAInitiatorCookie = _MtxrIkeSAInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 2),
    _MtxrIkeSAInitiatorCookie_Type()
)
mtxrIkeSAInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAInitiatorCookie.setStatus("current")
_MtxrIkeSAResponderCookie_Type = IsakmpCookie
_MtxrIkeSAResponderCookie_Object = MibTableColumn
mtxrIkeSAResponderCookie = _MtxrIkeSAResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 3),
    _MtxrIkeSAResponderCookie_Type()
)
mtxrIkeSAResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAResponderCookie.setStatus("current")
_MtxrIkeSAResponder_Type = BoolValue
_MtxrIkeSAResponder_Object = MibTableColumn
mtxrIkeSAResponder = _MtxrIkeSAResponder_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 4),
    _MtxrIkeSAResponder_Type()
)
mtxrIkeSAResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAResponder.setStatus("current")
_MtxrIkeSANatt_Type = BoolValue
_MtxrIkeSANatt_Object = MibTableColumn
mtxrIkeSANatt = _MtxrIkeSANatt_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 5),
    _MtxrIkeSANatt_Type()
)
mtxrIkeSANatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSANatt.setStatus("current")
_MtxrIkeSAVersion_Type = Gauge32
_MtxrIkeSAVersion_Object = MibTableColumn
mtxrIkeSAVersion = _MtxrIkeSAVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 6),
    _MtxrIkeSAVersion_Type()
)
mtxrIkeSAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAVersion.setStatus("current")


class _MtxrIkeSAState_Type(Integer32):
    """Custom type mtxrIkeSAState based on Integer32"""
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
        *(("exchange", 1),
          ("established", 2),
          ("expired", 3),
          ("eap", 4))
    )


_MtxrIkeSAState_Type.__name__ = "Integer32"
_MtxrIkeSAState_Object = MibTableColumn
mtxrIkeSAState = _MtxrIkeSAState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 7),
    _MtxrIkeSAState_Type()
)
mtxrIkeSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAState.setStatus("current")
_MtxrIkeSAUptime_Type = TimeTicks
_MtxrIkeSAUptime_Object = MibTableColumn
mtxrIkeSAUptime = _MtxrIkeSAUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 8),
    _MtxrIkeSAUptime_Type()
)
mtxrIkeSAUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAUptime.setStatus("current")
_MtxrIkeSASeen_Type = TimeTicks
_MtxrIkeSASeen_Object = MibTableColumn
mtxrIkeSASeen = _MtxrIkeSASeen_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 9),
    _MtxrIkeSASeen_Type()
)
mtxrIkeSASeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSASeen.setStatus("current")
_MtxrIkeSAIdentity_Type = DisplayString
_MtxrIkeSAIdentity_Object = MibTableColumn
mtxrIkeSAIdentity = _MtxrIkeSAIdentity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 10),
    _MtxrIkeSAIdentity_Type()
)
mtxrIkeSAIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAIdentity.setStatus("current")
_MtxrIkeSAPh2Count_Type = Gauge32
_MtxrIkeSAPh2Count_Object = MibTableColumn
mtxrIkeSAPh2Count = _MtxrIkeSAPh2Count_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 11),
    _MtxrIkeSAPh2Count_Type()
)
mtxrIkeSAPh2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAPh2Count.setStatus("current")
_MtxrIkeSALocalAddressType_Type = InetAddressType
_MtxrIkeSALocalAddressType_Object = MibTableColumn
mtxrIkeSALocalAddressType = _MtxrIkeSALocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 12),
    _MtxrIkeSALocalAddressType_Type()
)
mtxrIkeSALocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSALocalAddressType.setStatus("current")
_MtxrIkeSALocalAddress_Type = InetAddress
_MtxrIkeSALocalAddress_Object = MibTableColumn
mtxrIkeSALocalAddress = _MtxrIkeSALocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 13),
    _MtxrIkeSALocalAddress_Type()
)
mtxrIkeSALocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSALocalAddress.setStatus("current")
_MtxrIkeSALocalPort_Type = InetPortNumber
_MtxrIkeSALocalPort_Object = MibTableColumn
mtxrIkeSALocalPort = _MtxrIkeSALocalPort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 14),
    _MtxrIkeSALocalPort_Type()
)
mtxrIkeSALocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSALocalPort.setStatus("current")
_MtxrIkeSAPeerAddressType_Type = InetAddressType
_MtxrIkeSAPeerAddressType_Object = MibTableColumn
mtxrIkeSAPeerAddressType = _MtxrIkeSAPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 15),
    _MtxrIkeSAPeerAddressType_Type()
)
mtxrIkeSAPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAPeerAddressType.setStatus("current")
_MtxrIkeSAPeerAddress_Type = InetAddress
_MtxrIkeSAPeerAddress_Object = MibTableColumn
mtxrIkeSAPeerAddress = _MtxrIkeSAPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 16),
    _MtxrIkeSAPeerAddress_Type()
)
mtxrIkeSAPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAPeerAddress.setStatus("current")
_MtxrIkeSAPeerPort_Type = InetPortNumber
_MtxrIkeSAPeerPort_Object = MibTableColumn
mtxrIkeSAPeerPort = _MtxrIkeSAPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 17),
    _MtxrIkeSAPeerPort_Type()
)
mtxrIkeSAPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSAPeerPort.setStatus("current")
_MtxrIkeSADynamicAddressType_Type = InetAddressType
_MtxrIkeSADynamicAddressType_Object = MibTableColumn
mtxrIkeSADynamicAddressType = _MtxrIkeSADynamicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 18),
    _MtxrIkeSADynamicAddressType_Type()
)
mtxrIkeSADynamicAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSADynamicAddressType.setStatus("current")
_MtxrIkeSADynamicAddress_Type = InetAddress
_MtxrIkeSADynamicAddress_Object = MibTableColumn
mtxrIkeSADynamicAddress = _MtxrIkeSADynamicAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 19),
    _MtxrIkeSADynamicAddress_Type()
)
mtxrIkeSADynamicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSADynamicAddress.setStatus("current")
_MtxrIkeSATxBytes_Type = Counter64
_MtxrIkeSATxBytes_Object = MibTableColumn
mtxrIkeSATxBytes = _MtxrIkeSATxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 20),
    _MtxrIkeSATxBytes_Type()
)
mtxrIkeSATxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSATxBytes.setStatus("current")
_MtxrIkeSARxBytes_Type = Counter64
_MtxrIkeSARxBytes_Object = MibTableColumn
mtxrIkeSARxBytes = _MtxrIkeSARxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 21),
    _MtxrIkeSARxBytes_Type()
)
mtxrIkeSARxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSARxBytes.setStatus("current")
_MtxrIkeSATxPackets_Type = Counter64
_MtxrIkeSATxPackets_Object = MibTableColumn
mtxrIkeSATxPackets = _MtxrIkeSATxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 22),
    _MtxrIkeSATxPackets_Type()
)
mtxrIkeSATxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSATxPackets.setStatus("current")
_MtxrIkeSARxPackets_Type = Counter64
_MtxrIkeSARxPackets_Object = MibTableColumn
mtxrIkeSARxPackets = _MtxrIkeSARxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 20, 2, 1, 23),
    _MtxrIkeSARxPackets_Type()
)
mtxrIkeSARxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrIkeSARxPackets.setStatus("current")
_MtxrWifi_ObjectIdentity = ObjectIdentity
mtxrWifi = _MtxrWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21)
)
_MtxrWifiCapsman_ObjectIdentity = ObjectIdentity
mtxrWifiCapsman = _MtxrWifiCapsman_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1)
)
_MtxrWifiCapsmanEnabled_Type = TruthValue
_MtxrWifiCapsmanEnabled_Object = MibScalar
mtxrWifiCapsmanEnabled = _MtxrWifiCapsmanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 1),
    _MtxrWifiCapsmanEnabled_Type()
)
mtxrWifiCapsmanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanEnabled.setStatus("current")
_MtxrWifiCapsmanInterfaces_Type = DisplayString
_MtxrWifiCapsmanInterfaces_Object = MibScalar
mtxrWifiCapsmanInterfaces = _MtxrWifiCapsmanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 2),
    _MtxrWifiCapsmanInterfaces_Type()
)
mtxrWifiCapsmanInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanInterfaces.setStatus("current")
_MtxrWifiCapsmanCACertificate_Type = DisplayString
_MtxrWifiCapsmanCACertificate_Object = MibScalar
mtxrWifiCapsmanCACertificate = _MtxrWifiCapsmanCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 3),
    _MtxrWifiCapsmanCACertificate_Type()
)
mtxrWifiCapsmanCACertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanCACertificate.setStatus("current")
_MtxrWifiCapsmanCertificate_Type = DisplayString
_MtxrWifiCapsmanCertificate_Object = MibScalar
mtxrWifiCapsmanCertificate = _MtxrWifiCapsmanCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 4),
    _MtxrWifiCapsmanCertificate_Type()
)
mtxrWifiCapsmanCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanCertificate.setStatus("current")
_MtxrWifiCapsmanRequirePeerCertificate_Type = TruthValue
_MtxrWifiCapsmanRequirePeerCertificate_Object = MibScalar
mtxrWifiCapsmanRequirePeerCertificate = _MtxrWifiCapsmanRequirePeerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 5),
    _MtxrWifiCapsmanRequirePeerCertificate_Type()
)
mtxrWifiCapsmanRequirePeerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanRequirePeerCertificate.setStatus("current")
_MtxrWifiCapsmanPackagePath_Type = DisplayString
_MtxrWifiCapsmanPackagePath_Object = MibScalar
mtxrWifiCapsmanPackagePath = _MtxrWifiCapsmanPackagePath_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 6),
    _MtxrWifiCapsmanPackagePath_Type()
)
mtxrWifiCapsmanPackagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanPackagePath.setStatus("current")
_MtxrWifiCapsmanUpgradePolicy_Type = Integer32
_MtxrWifiCapsmanUpgradePolicy_Object = MibScalar
mtxrWifiCapsmanUpgradePolicy = _MtxrWifiCapsmanUpgradePolicy_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 7),
    _MtxrWifiCapsmanUpgradePolicy_Type()
)
mtxrWifiCapsmanUpgradePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanUpgradePolicy.setStatus("current")
_MtxrWifiCapsmanGeneratedCaCertificate_Type = DisplayString
_MtxrWifiCapsmanGeneratedCaCertificate_Object = MibScalar
mtxrWifiCapsmanGeneratedCaCertificate = _MtxrWifiCapsmanGeneratedCaCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 8),
    _MtxrWifiCapsmanGeneratedCaCertificate_Type()
)
mtxrWifiCapsmanGeneratedCaCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanGeneratedCaCertificate.setStatus("current")
_MtxrWifiCapsmanGeneratedCertificate_Type = DisplayString
_MtxrWifiCapsmanGeneratedCertificate_Object = MibScalar
mtxrWifiCapsmanGeneratedCertificate = _MtxrWifiCapsmanGeneratedCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 1, 9),
    _MtxrWifiCapsmanGeneratedCertificate_Type()
)
mtxrWifiCapsmanGeneratedCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiCapsmanGeneratedCertificate.setStatus("current")
_MtxrWifiCap_ObjectIdentity = ObjectIdentity
mtxrWifiCap = _MtxrWifiCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2)
)
_MtxrCapEnabled_Type = TruthValue
_MtxrCapEnabled_Object = MibScalar
mtxrCapEnabled = _MtxrCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 1),
    _MtxrCapEnabled_Type()
)
mtxrCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapEnabled.setStatus("current")
_MtxrCapInterfaces_Type = DisplayString
_MtxrCapInterfaces_Object = MibScalar
mtxrCapInterfaces = _MtxrCapInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 2),
    _MtxrCapInterfaces_Type()
)
mtxrCapInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapInterfaces.setStatus("current")
_MtxrCapCertificate_Type = DisplayString
_MtxrCapCertificate_Object = MibScalar
mtxrCapCertificate = _MtxrCapCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 3),
    _MtxrCapCertificate_Type()
)
mtxrCapCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCertificate.setStatus("current")
_MtxrCapCapsManAddresses_Type = DisplayString
_MtxrCapCapsManAddresses_Object = MibScalar
mtxrCapCapsManAddresses = _MtxrCapCapsManAddresses_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 4),
    _MtxrCapCapsManAddresses_Type()
)
mtxrCapCapsManAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCapsManAddresses.setStatus("current")
_MtxrCapCapsManNames_Type = DisplayString
_MtxrCapCapsManNames_Object = MibScalar
mtxrCapCapsManNames = _MtxrCapCapsManNames_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 5),
    _MtxrCapCapsManNames_Type()
)
mtxrCapCapsManNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCapsManNames.setStatus("current")
_MtxrCapCapsManCertificateCommonNames_Type = DisplayString
_MtxrCapCapsManCertificateCommonNames_Object = MibScalar
mtxrCapCapsManCertificateCommonNames = _MtxrCapCapsManCertificateCommonNames_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 6),
    _MtxrCapCapsManCertificateCommonNames_Type()
)
mtxrCapCapsManCertificateCommonNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCapsManCertificateCommonNames.setStatus("current")
_MtxrCapLockToCapsMan_Type = TruthValue
_MtxrCapLockToCapsMan_Object = MibScalar
mtxrCapLockToCapsMan = _MtxrCapLockToCapsMan_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 7),
    _MtxrCapLockToCapsMan_Type()
)
mtxrCapLockToCapsMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapLockToCapsMan.setStatus("current")
_MtxrCapSlavesStatic_Type = TruthValue
_MtxrCapSlavesStatic_Object = MibScalar
mtxrCapSlavesStatic = _MtxrCapSlavesStatic_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 8),
    _MtxrCapSlavesStatic_Type()
)
mtxrCapSlavesStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapSlavesStatic.setStatus("current")
_MtxrCapSlavesDatapath_Type = DisplayString
_MtxrCapSlavesDatapath_Object = MibScalar
mtxrCapSlavesDatapath = _MtxrCapSlavesDatapath_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 9),
    _MtxrCapSlavesDatapath_Type()
)
mtxrCapSlavesDatapath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapSlavesDatapath.setStatus("current")
_MtxrCapRequestedCertificate_Type = DisplayString
_MtxrCapRequestedCertificate_Object = MibScalar
mtxrCapRequestedCertificate = _MtxrCapRequestedCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 10),
    _MtxrCapRequestedCertificate_Type()
)
mtxrCapRequestedCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapRequestedCertificate.setStatus("current")
_MtxrCapLockedCapsManCommonName_Type = DisplayString
_MtxrCapLockedCapsManCommonName_Object = MibScalar
mtxrCapLockedCapsManCommonName = _MtxrCapLockedCapsManCommonName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 11),
    _MtxrCapLockedCapsManCommonName_Type()
)
mtxrCapLockedCapsManCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapLockedCapsManCommonName.setStatus("current")
_MtxrCapCurrentCapsManAddress_Type = DisplayString
_MtxrCapCurrentCapsManAddress_Object = MibScalar
mtxrCapCurrentCapsManAddress = _MtxrCapCurrentCapsManAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 12),
    _MtxrCapCurrentCapsManAddress_Type()
)
mtxrCapCurrentCapsManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCurrentCapsManAddress.setStatus("current")
_MtxrCapCurrentCapsManIdentity_Type = DisplayString
_MtxrCapCurrentCapsManIdentity_Object = MibScalar
mtxrCapCurrentCapsManIdentity = _MtxrCapCurrentCapsManIdentity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 2, 13),
    _MtxrCapCurrentCapsManIdentity_Type()
)
mtxrCapCurrentCapsManIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCapCurrentCapsManIdentity.setStatus("current")
_MtxrRemoteCapTable_Object = MibTable
mtxrRemoteCapTable = _MtxrRemoteCapTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3)
)
if mibBuilder.loadTexts:
    mtxrRemoteCapTable.setStatus("current")
_MtxrWifiRemoteCapEntry_Object = MibTableRow
mtxrWifiRemoteCapEntry = _MtxrWifiRemoteCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1)
)
mtxrWifiRemoteCapEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrRemoteCapId"),
)
if mibBuilder.loadTexts:
    mtxrWifiRemoteCapEntry.setStatus("current")
_MtxrRemoteCapId_Type = ObjectIndex
_MtxrRemoteCapId_Object = MibTableColumn
mtxrRemoteCapId = _MtxrRemoteCapId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 1),
    _MtxrRemoteCapId_Type()
)
mtxrRemoteCapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrRemoteCapId.setStatus("current")
_MtxrRemoteCapAddress_Type = DisplayString
_MtxrRemoteCapAddress_Object = MibTableColumn
mtxrRemoteCapAddress = _MtxrRemoteCapAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 2),
    _MtxrRemoteCapAddress_Type()
)
mtxrRemoteCapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapAddress.setStatus("current")
_MtxrRemoteCapIdentity_Type = DisplayString
_MtxrRemoteCapIdentity_Object = MibTableColumn
mtxrRemoteCapIdentity = _MtxrRemoteCapIdentity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 3),
    _MtxrRemoteCapIdentity_Type()
)
mtxrRemoteCapIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapIdentity.setStatus("current")
_MtxrRemoteCapBoardName_Type = DisplayString
_MtxrRemoteCapBoardName_Object = MibTableColumn
mtxrRemoteCapBoardName = _MtxrRemoteCapBoardName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 4),
    _MtxrRemoteCapBoardName_Type()
)
mtxrRemoteCapBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapBoardName.setStatus("current")
_MtxrRemoteCapSerial_Type = DisplayString
_MtxrRemoteCapSerial_Object = MibTableColumn
mtxrRemoteCapSerial = _MtxrRemoteCapSerial_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 5),
    _MtxrRemoteCapSerial_Type()
)
mtxrRemoteCapSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapSerial.setStatus("current")
_MtxrRemoteCapVersion_Type = DisplayString
_MtxrRemoteCapVersion_Object = MibTableColumn
mtxrRemoteCapVersion = _MtxrRemoteCapVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 6),
    _MtxrRemoteCapVersion_Type()
)
mtxrRemoteCapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapVersion.setStatus("current")
_MtxrRemoteCapBaseMac_Type = MacAddress
_MtxrRemoteCapBaseMac_Object = MibTableColumn
mtxrRemoteCapBaseMac = _MtxrRemoteCapBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 7),
    _MtxrRemoteCapBaseMac_Type()
)
mtxrRemoteCapBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapBaseMac.setStatus("current")
_MtxrRemoteCapCommonName_Type = DisplayString
_MtxrRemoteCapCommonName_Object = MibTableColumn
mtxrRemoteCapCommonName = _MtxrRemoteCapCommonName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 8),
    _MtxrRemoteCapCommonName_Type()
)
mtxrRemoteCapCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapCommonName.setStatus("current")
_MtxrRemoteCapState_Type = DisplayString
_MtxrRemoteCapState_Object = MibTableColumn
mtxrRemoteCapState = _MtxrRemoteCapState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 3, 1, 9),
    _MtxrRemoteCapState_Type()
)
mtxrRemoteCapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrRemoteCapState.setStatus("current")
_MtxrWifiRegistrationTable_Object = MibTable
mtxrWifiRegistrationTable = _MtxrWifiRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4)
)
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTable.setStatus("current")
_MtxrWifiRegistrationTableEntry_Object = MibTableRow
mtxrWifiRegistrationTableEntry = _MtxrWifiRegistrationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1)
)
mtxrWifiRegistrationTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWifiRegistrationMacAddress"),
    (0, "MIKROTIK-MIB", "mtxrWifiRegistrationInterface"),
)
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTableEntry.setStatus("current")
_MtxrWifiRegistrationMacAddress_Type = MacAddress
_MtxrWifiRegistrationMacAddress_Object = MibTableColumn
mtxrWifiRegistrationMacAddress = _MtxrWifiRegistrationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 1),
    _MtxrWifiRegistrationMacAddress_Type()
)
mtxrWifiRegistrationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationMacAddress.setStatus("current")
_MtxrWifiRegistrationInterface_Type = ObjectIndex
_MtxrWifiRegistrationInterface_Object = MibTableColumn
mtxrWifiRegistrationInterface = _MtxrWifiRegistrationInterface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 2),
    _MtxrWifiRegistrationInterface_Type()
)
mtxrWifiRegistrationInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationInterface.setStatus("current")
_MtxrWifiRegistrationSsid_Type = DisplayString
_MtxrWifiRegistrationSsid_Object = MibTableColumn
mtxrWifiRegistrationSsid = _MtxrWifiRegistrationSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 3),
    _MtxrWifiRegistrationSsid_Type()
)
mtxrWifiRegistrationSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationSsid.setStatus("current")
_MtxrWifiRegistrationUptime_Type = TimeTicks
_MtxrWifiRegistrationUptime_Object = MibTableColumn
mtxrWifiRegistrationUptime = _MtxrWifiRegistrationUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 4),
    _MtxrWifiRegistrationUptime_Type()
)
mtxrWifiRegistrationUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationUptime.setStatus("current")
_MtxrWifiRegistrationLastActivity_Type = Integer32
_MtxrWifiRegistrationLastActivity_Object = MibTableColumn
mtxrWifiRegistrationLastActivity = _MtxrWifiRegistrationLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 5),
    _MtxrWifiRegistrationLastActivity_Type()
)
mtxrWifiRegistrationLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationLastActivity.setStatus("current")
_MtxrWifiRegistrationSignal_Type = Integer32
_MtxrWifiRegistrationSignal_Object = MibTableColumn
mtxrWifiRegistrationSignal = _MtxrWifiRegistrationSignal_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 6),
    _MtxrWifiRegistrationSignal_Type()
)
mtxrWifiRegistrationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationSignal.setStatus("current")
_MtxrWifiRegistrationAuthType_Type = DisplayString
_MtxrWifiRegistrationAuthType_Object = MibTableColumn
mtxrWifiRegistrationAuthType = _MtxrWifiRegistrationAuthType_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 7),
    _MtxrWifiRegistrationAuthType_Type()
)
mtxrWifiRegistrationAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationAuthType.setStatus("current")
_MtxrWifiRegistrationBand_Type = DisplayString
_MtxrWifiRegistrationBand_Object = MibTableColumn
mtxrWifiRegistrationBand = _MtxrWifiRegistrationBand_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 8),
    _MtxrWifiRegistrationBand_Type()
)
mtxrWifiRegistrationBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationBand.setStatus("current")
_MtxrWifiRegistrationTxRate_Type = Gauge32
_MtxrWifiRegistrationTxRate_Object = MibTableColumn
mtxrWifiRegistrationTxRate = _MtxrWifiRegistrationTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 9),
    _MtxrWifiRegistrationTxRate_Type()
)
mtxrWifiRegistrationTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTxRate.setStatus("current")
_MtxrWifiRegistrationRxRate_Type = Gauge32
_MtxrWifiRegistrationRxRate_Object = MibTableColumn
mtxrWifiRegistrationRxRate = _MtxrWifiRegistrationRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 10),
    _MtxrWifiRegistrationRxRate_Type()
)
mtxrWifiRegistrationRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationRxRate.setStatus("current")
_MtxrWifiRegistrationTxPackets_Type = Counter64
_MtxrWifiRegistrationTxPackets_Object = MibTableColumn
mtxrWifiRegistrationTxPackets = _MtxrWifiRegistrationTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 11),
    _MtxrWifiRegistrationTxPackets_Type()
)
mtxrWifiRegistrationTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTxPackets.setStatus("current")
_MtxrWifiRegistrationRxPackets_Type = Counter64
_MtxrWifiRegistrationRxPackets_Object = MibTableColumn
mtxrWifiRegistrationRxPackets = _MtxrWifiRegistrationRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 12),
    _MtxrWifiRegistrationRxPackets_Type()
)
mtxrWifiRegistrationRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationRxPackets.setStatus("current")
_MtxrWifiRegistrationTxBytes_Type = Counter64
_MtxrWifiRegistrationTxBytes_Object = MibTableColumn
mtxrWifiRegistrationTxBytes = _MtxrWifiRegistrationTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 13),
    _MtxrWifiRegistrationTxBytes_Type()
)
mtxrWifiRegistrationTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTxBytes.setStatus("current")
_MtxrWifiRegistrationRxBytes_Type = Counter64
_MtxrWifiRegistrationRxBytes_Object = MibTableColumn
mtxrWifiRegistrationRxBytes = _MtxrWifiRegistrationRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 14),
    _MtxrWifiRegistrationRxBytes_Type()
)
mtxrWifiRegistrationRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationRxBytes.setStatus("current")
_MtxrWifiRegistrationTxBitsPerSecond_Type = Integer32
_MtxrWifiRegistrationTxBitsPerSecond_Object = MibTableColumn
mtxrWifiRegistrationTxBitsPerSecond = _MtxrWifiRegistrationTxBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 15),
    _MtxrWifiRegistrationTxBitsPerSecond_Type()
)
mtxrWifiRegistrationTxBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationTxBitsPerSecond.setStatus("current")
_MtxrWifiRegistrationRxBitsPerSecond_Type = Integer32
_MtxrWifiRegistrationRxBitsPerSecond_Object = MibTableColumn
mtxrWifiRegistrationRxBitsPerSecond = _MtxrWifiRegistrationRxBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 16),
    _MtxrWifiRegistrationRxBitsPerSecond_Type()
)
mtxrWifiRegistrationRxBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationRxBitsPerSecond.setStatus("current")
_MtxrWifiRegistrationVlanId_Type = Integer32
_MtxrWifiRegistrationVlanId_Object = MibTableColumn
mtxrWifiRegistrationVlanId = _MtxrWifiRegistrationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 17),
    _MtxrWifiRegistrationVlanId_Type()
)
mtxrWifiRegistrationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationVlanId.setStatus("current")
_MtxrWifiRegistrationAuthorized_Type = TruthValue
_MtxrWifiRegistrationAuthorized_Object = MibTableColumn
mtxrWifiRegistrationAuthorized = _MtxrWifiRegistrationAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 4, 1, 18),
    _MtxrWifiRegistrationAuthorized_Type()
)
mtxrWifiRegistrationAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiRegistrationAuthorized.setStatus("current")
_MtxrWifiInterfaces_Object = MibTable
mtxrWifiInterfaces = _MtxrWifiInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5)
)
if mibBuilder.loadTexts:
    mtxrWifiInterfaces.setStatus("current")
_MtxrWifiInterfacesEntry_Object = MibTableRow
mtxrWifiInterfacesEntry = _MtxrWifiInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5, 1)
)
mtxrWifiInterfacesEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWifiInterfacesId"),
)
if mibBuilder.loadTexts:
    mtxrWifiInterfacesEntry.setStatus("current")
_MtxrWifiInterfacesId_Type = ObjectIndex
_MtxrWifiInterfacesId_Object = MibTableColumn
mtxrWifiInterfacesId = _MtxrWifiInterfacesId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5, 1, 1),
    _MtxrWifiInterfacesId_Type()
)
mtxrWifiInterfacesId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWifiInterfacesId.setStatus("current")
_MtxrWifiInterfacesName_Type = DisplayString
_MtxrWifiInterfacesName_Object = MibTableColumn
mtxrWifiInterfacesName = _MtxrWifiInterfacesName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5, 1, 2),
    _MtxrWifiInterfacesName_Type()
)
mtxrWifiInterfacesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiInterfacesName.setStatus("current")
_MtxrWifiInterfacesSsid_Type = DisplayString
_MtxrWifiInterfacesSsid_Object = MibTableColumn
mtxrWifiInterfacesSsid = _MtxrWifiInterfacesSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5, 1, 3),
    _MtxrWifiInterfacesSsid_Type()
)
mtxrWifiInterfacesSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiInterfacesSsid.setStatus("current")
_MtxrWifiInterfacesFreq_Type = DisplayString
_MtxrWifiInterfacesFreq_Object = MibTableColumn
mtxrWifiInterfacesFreq = _MtxrWifiInterfacesFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 21, 5, 1, 4),
    _MtxrWifiInterfacesFreq_Type()
)
mtxrWifiInterfacesFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWifiInterfacesFreq.setStatus("current")
_MtxrCT_ObjectIdentity = ObjectIdentity
mtxrCT = _MtxrCT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 22)
)
_MtxrCtTotalEntries_Type = Counter32
_MtxrCtTotalEntries_Object = MibScalar
mtxrCtTotalEntries = _MtxrCtTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 22, 1, 1),
    _MtxrCtTotalEntries_Type()
)
mtxrCtTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCtTotalEntries.setStatus("current")
_MtxrCtIP4Entries_Type = Counter32
_MtxrCtIP4Entries_Object = MibScalar
mtxrCtIP4Entries = _MtxrCtIP4Entries_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 22, 1, 2),
    _MtxrCtIP4Entries_Type()
)
mtxrCtIP4Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCtIP4Entries.setStatus("current")
_MtxrCtIP6Entries_Type = Counter32
_MtxrCtIP6Entries_Object = MibScalar
mtxrCtIP6Entries = _MtxrCtIP6Entries_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 22, 1, 3),
    _MtxrCtIP6Entries_Type()
)
mtxrCtIP6Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrCtIP6Entries.setStatus("current")
_MtXMetaInfo_ObjectIdentity = ObjectIdentity
mtXMetaInfo = _MtXMetaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2)
)
_MtXRouterOsGroups_ObjectIdentity = ObjectIdentity
mtXRouterOsGroups = _MtXRouterOsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1)
)

# Managed Objects groups

mtxrCtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 22, 1)
)
mtxrCtStatsGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrCtTotalEntries"),
        ("MIKROTIK-MIB", "mtxrCtIP4Entries"),
        ("MIKROTIK-MIB", "mtxrCtIP6Entries"))
)
if mibBuilder.loadTexts:
    mtxrCtStatsGroup.setStatus("current")

mtxrWirelessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 1)
)
mtxrWirelessGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrWlStatTxRate"),
        ("MIKROTIK-MIB", "mtxrWlStatRxRate"),
        ("MIKROTIK-MIB", "mtxrWlStatStrength"),
        ("MIKROTIK-MIB", "mtxrWlStatSsid"),
        ("MIKROTIK-MIB", "mtxrWlStatBssid"),
        ("MIKROTIK-MIB", "mtxrWlStatFreq"),
        ("MIKROTIK-MIB", "mtxrWlStatBand"),
        ("MIKROTIK-MIB", "mtxrWlStatTxCCQ"),
        ("MIKROTIK-MIB", "mtxrWlStatRxCCQ"),
        ("MIKROTIK-MIB", "mtxrWlRtabStrength"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxBytes"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxBytes"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxPackets"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxPackets"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxRate"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxRate"),
        ("MIKROTIK-MIB", "mtxrWlRtabEntryCount"),
        ("MIKROTIK-MIB", "mtxrWlRtabRouterOSVersion"),
        ("MIKROTIK-MIB", "mtxrWlRtabUptime"),
        ("MIKROTIK-MIB", "mtxrWlRtabSignalToNoise"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh0"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh0"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh1"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh1"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh2"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh2"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrength"),
        ("MIKROTIK-MIB", "mtxrWlRtabRadioName"),
        ("MIKROTIK-MIB", "mtxrWlApTxRate"),
        ("MIKROTIK-MIB", "mtxrWlApRxRate"),
        ("MIKROTIK-MIB", "mtxrWlApSsid"),
        ("MIKROTIK-MIB", "mtxrWlApBssid"),
        ("MIKROTIK-MIB", "mtxrWlApClientCount"),
        ("MIKROTIK-MIB", "mtxrWlApBand"),
        ("MIKROTIK-MIB", "mtxrWlApFreq"),
        ("MIKROTIK-MIB", "mtxrWlApNoiseFloor"),
        ("MIKROTIK-MIB", "mtxrWlApOverallTxCCQ"),
        ("MIKROTIK-MIB", "mtxrWlApAuthClientCount"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabAddr"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxBytes"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxBytes"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxPackets"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxPackets"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxRate"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxRate"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabUptime"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxStrength"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxStrength"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabSsid"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabEntryCount"),
        ("MIKROTIK-MIB", "mtxrWlCMREntryCount"),
        ("MIKROTIK-MIB", "mtxrWlCMRegClientCount"),
        ("MIKROTIK-MIB", "mtxrWlCMAuthClientCount"),
        ("MIKROTIK-MIB", "mtxrWl60GMode"),
        ("MIKROTIK-MIB", "mtxrWl60GSsid"),
        ("MIKROTIK-MIB", "mtxrWl60GConnected"),
        ("MIKROTIK-MIB", "mtxrWl60GRemote"),
        ("MIKROTIK-MIB", "mtxrWl60GFreq"),
        ("MIKROTIK-MIB", "mtxrWl60GMcs"),
        ("MIKROTIK-MIB", "mtxrWl60GSignal"),
        ("MIKROTIK-MIB", "mtxrWl60GTxSector"),
        ("MIKROTIK-MIB", "mtxrWl60GTxSectorInfo"),
        ("MIKROTIK-MIB", "mtxrWl60GRssi"),
        ("MIKROTIK-MIB", "mtxrWl60GPhyRate"),
        ("MIKROTIK-MIB", "mtxrWl60GStaConnected"),
        ("MIKROTIK-MIB", "mtxrWl60GStaRemote"),
        ("MIKROTIK-MIB", "mtxrWl60GStaMcs"),
        ("MIKROTIK-MIB", "mtxrWl60GStaSignal"),
        ("MIKROTIK-MIB", "mtxrWl60GStaTxSector"))
)
if mibBuilder.loadTexts:
    mtxrWirelessGroup.setStatus("current")

mtxrQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 2)
)
mtxrQueueGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrQueueSimpleName"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleSrcAddr"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleSrcMask"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDstAddr"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDstMask"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleIface"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleBytesIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleBytesOut"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePacketsIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePacketsOut"),
        ("MIKROTIK-MIB", "mtxrQueueTreeName"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePCQQueuesIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePCQQueuesOut"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDroppedIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDroppedOut"),
        ("MIKROTIK-MIB", "mtxrQueueTreeFlow"),
        ("MIKROTIK-MIB", "mtxrQueueTreeParentIndex"),
        ("MIKROTIK-MIB", "mtxrQueueTreeBytes"),
        ("MIKROTIK-MIB", "mtxrQueueTreePackets"),
        ("MIKROTIK-MIB", "mtxrQueueTreeHCBytes"),
        ("MIKROTIK-MIB", "mtxrQueueTreePCQQueues"),
        ("MIKROTIK-MIB", "mtxrQueueTreeDropped"))
)
if mibBuilder.loadTexts:
    mtxrQueueGroup.setStatus("current")

mtxrHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 3)
)
mtxrHealthGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrHlCoreVoltage"),
        ("MIKROTIK-MIB", "mtxrHlThreeDotThreeVoltage"),
        ("MIKROTIK-MIB", "mtxrHlFiveVoltage"),
        ("MIKROTIK-MIB", "mtxrHlTwelveVoltage"),
        ("MIKROTIK-MIB", "mtxrHlSensorTemperature"),
        ("MIKROTIK-MIB", "mtxrHlCpuTemperature"),
        ("MIKROTIK-MIB", "mtxrHlBoardTemperature"),
        ("MIKROTIK-MIB", "mtxrHlVoltage"),
        ("MIKROTIK-MIB", "mtxrHlActiveFan"),
        ("MIKROTIK-MIB", "mtxrHlTemperature"),
        ("MIKROTIK-MIB", "mtxrHlProcessorTemperature"),
        ("MIKROTIK-MIB", "mtxrHlCurrent"),
        ("MIKROTIK-MIB", "mtxrHlPower"),
        ("MIKROTIK-MIB", "mtxrHlProcessorFrequency"),
        ("MIKROTIK-MIB", "mtxrHlPowerSupplyState"),
        ("MIKROTIK-MIB", "mtxrHlBackupPowerSupplyState"),
        ("MIKROTIK-MIB", "mtxrHlFanSpeed1"),
        ("MIKROTIK-MIB", "mtxrHlFanSpeed2"),
        ("MIKROTIK-MIB", "mtxrAlarmSocketStatus"),
        ("MIKROTIK-MIB", "mtxrGaugeName"),
        ("MIKROTIK-MIB", "mtxrGaugeValue"),
        ("MIKROTIK-MIB", "mtxrGaugeUnit"))
)
if mibBuilder.loadTexts:
    mtxrHealthGroup.setStatus("current")

mtxrLincenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 4)
)
mtxrLincenseGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrLicSoftwareId"),
        ("MIKROTIK-MIB", "mtxrLicUpgrUntil"),
        ("MIKROTIK-MIB", "mtxrLicLevel"),
        ("MIKROTIK-MIB", "mtxrLicVersion"),
        ("MIKROTIK-MIB", "mtxrLicUpgradableTo"))
)
if mibBuilder.loadTexts:
    mtxrLincenseGroup.setStatus("current")

mtxrHotspotActiveUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 5)
)
mtxrHotspotActiveUserGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrHotspotActiveUserServerID"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserName"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserDomain"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIP"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserMAC"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserConnectTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserValidTillTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIdleStartTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIdleTimeout"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPingTimeout"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBytesIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBytesOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPacketsIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPacketsOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserLimitBytesIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserLimitBytesOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserAdvertStatus"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserRadius"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBlockedByAdvert"))
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserGroup.setStatus("current")

mtxrOpticalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 6)
)
mtxrOpticalGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrOpticalName"),
        ("MIKROTIK-MIB", "mtxrOpticalRxLoss"),
        ("MIKROTIK-MIB", "mtxrOpticalTxFault"),
        ("MIKROTIK-MIB", "mtxrOpticalWavelength"),
        ("MIKROTIK-MIB", "mtxrOpticalTemperature"),
        ("MIKROTIK-MIB", "mtxrOpticalSupplyVoltage"),
        ("MIKROTIK-MIB", "mtxrOpticalTxBiasCurrent"),
        ("MIKROTIK-MIB", "mtxrOpticalTxPower"),
        ("MIKROTIK-MIB", "mtxrOpticalRxPower"),
        ("MIKROTIK-MIB", "mtxrOpticalVendorName"),
        ("MIKROTIK-MIB", "mtxrOpticalVendorSerial"))
)
if mibBuilder.loadTexts:
    mtxrOpticalGroup.setStatus("current")

mtxrIkeSAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 7)
)
mtxrIkeSAGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrIkeSACount"),
        ("MIKROTIK-MIB", "mtxrIkeSAInitiatorCookie"),
        ("MIKROTIK-MIB", "mtxrIkeSAResponderCookie"),
        ("MIKROTIK-MIB", "mtxrIkeSAResponder"),
        ("MIKROTIK-MIB", "mtxrIkeSANatt"),
        ("MIKROTIK-MIB", "mtxrIkeSAVersion"),
        ("MIKROTIK-MIB", "mtxrIkeSAState"),
        ("MIKROTIK-MIB", "mtxrIkeSAUptime"),
        ("MIKROTIK-MIB", "mtxrIkeSASeen"),
        ("MIKROTIK-MIB", "mtxrIkeSAIdentity"),
        ("MIKROTIK-MIB", "mtxrIkeSAPh2Count"),
        ("MIKROTIK-MIB", "mtxrIkeSALocalAddressType"),
        ("MIKROTIK-MIB", "mtxrIkeSALocalAddress"),
        ("MIKROTIK-MIB", "mtxrIkeSALocalPort"),
        ("MIKROTIK-MIB", "mtxrIkeSAPeerAddressType"),
        ("MIKROTIK-MIB", "mtxrIkeSAPeerAddress"),
        ("MIKROTIK-MIB", "mtxrIkeSAPeerPort"),
        ("MIKROTIK-MIB", "mtxrIkeSADynamicAddressType"),
        ("MIKROTIK-MIB", "mtxrIkeSADynamicAddress"),
        ("MIKROTIK-MIB", "mtxrIkeSATxBytes"),
        ("MIKROTIK-MIB", "mtxrIkeSARxBytes"),
        ("MIKROTIK-MIB", "mtxrIkeSATxPackets"),
        ("MIKROTIK-MIB", "mtxrIkeSARxPackets"))
)
if mibBuilder.loadTexts:
    mtxrIkeSAGroup.setStatus("current")

mtxrScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 8)
)
mtxrScriptGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrScriptName"),
        ("MIKROTIK-MIB", "mtxrScriptRunCmd"))
)
if mibBuilder.loadTexts:
    mtxrScriptGroup.setStatus("current")

mtxrNstremeDualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 10)
)
mtxrNstremeDualGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrDnStatTxRate"),
        ("MIKROTIK-MIB", "mtxrDnStatRxRate"),
        ("MIKROTIK-MIB", "mtxrDnStatTxStrength"),
        ("MIKROTIK-MIB", "mtxrDnStatRxStrength"),
        ("MIKROTIK-MIB", "mtxrDnConnected"))
)
if mibBuilder.loadTexts:
    mtxrNstremeDualGroup.setStatus("current")

mtxrNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 11)
)
mtxrNeighborGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrNeighborIpAddress"),
        ("MIKROTIK-MIB", "mtxrNeighborMacAddress"),
        ("MIKROTIK-MIB", "mtxrNeighborVersion"),
        ("MIKROTIK-MIB", "mtxrNeighborPlatform"),
        ("MIKROTIK-MIB", "mtxrNeighborIdentity"),
        ("MIKROTIK-MIB", "mtxrNeighborSoftwareID"),
        ("MIKROTIK-MIB", "mtxrNeighborInterfaceID"))
)
if mibBuilder.loadTexts:
    mtxrNeighborGroup.setStatus("current")

mtxrDHCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 12)
)
mtxrDHCPGroup.setObjects(
    ("MIKROTIK-MIB", "mtxrDHCPLeaseCount")
)
if mibBuilder.loadTexts:
    mtxrDHCPGroup.setStatus("current")

mtxrSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 13)
)
mtxrSystemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrSystemReboot"),
        ("MIKROTIK-MIB", "mtxrUSBPowerReset"),
        ("MIKROTIK-MIB", "mtxrSerialNumber"),
        ("MIKROTIK-MIB", "mtxrFirmwareVersion"),
        ("MIKROTIK-MIB", "mtxrNote"),
        ("MIKROTIK-MIB", "mtxrBuildTime"),
        ("MIKROTIK-MIB", "mtxrFirmwareUpgradeVersion"),
        ("MIKROTIK-MIB", "mtxrBoardName"))
)
if mibBuilder.loadTexts:
    mtxrSystemGroup.setStatus("current")

mtxrGPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 15)
)
mtxrGPSGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrDate"),
        ("MIKROTIK-MIB", "mtxrLongtitude"),
        ("MIKROTIK-MIB", "mtxrLatitude"),
        ("MIKROTIK-MIB", "mtxrAltitude"),
        ("MIKROTIK-MIB", "mtxrSpeed"),
        ("MIKROTIK-MIB", "mtxrSattelites"),
        ("MIKROTIK-MIB", "mtxrValid"))
)
if mibBuilder.loadTexts:
    mtxrGPSGroup.setStatus("current")

mtxrWirelessModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 16)
)
mtxrWirelessModemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrWirelessModemSignalStrength"),
        ("MIKROTIK-MIB", "mtxrWirelessModemSignalECIO"),
        ("MIKROTIK-MIB", "mtxrWirelessModemManufacturer"),
        ("MIKROTIK-MIB", "mtxrWirelessModemModel"),
        ("MIKROTIK-MIB", "mtxrWirelessModemRevision"),
        ("MIKROTIK-MIB", "mtxrWirelessModemIMEI"),
        ("MIKROTIK-MIB", "mtxrWirelessModemIMSI"),
        ("MIKROTIK-MIB", "mtxrWirelessModemAccessTechnology"),
        ("MIKROTIK-MIB", "mtxrWirelessModemFrameErrorRate"),
        ("MIKROTIK-MIB", "mtxrWirelessModemRSRP"),
        ("MIKROTIK-MIB", "mtxrWirelessModemRSRQ"),
        ("MIKROTIK-MIB", "mtxrWirelessModemSINR"),
        ("MIKROTIK-MIB", "mtxrWirelessModemPinStatus"))
)
if mibBuilder.loadTexts:
    mtxrWirelessModemGroup.setStatus("current")

mtxrInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 17)
)
mtxrInterfaceStatsGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrInterfaceStatsName"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverRxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverRxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverTxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverTxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxTooShort"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxTooLong"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxBroadcast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxPause"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxMulticast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxFCSError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxAlignError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxFragment"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxOverflow"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxControl"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxUnknownOp"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxLengthError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxCodeError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxCarrierError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxJabber"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxDrop"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTooShort"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTooLong"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxBroadcast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPause"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxMulticast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxUnderrun"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxExcessiveCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxMultipleCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxSingleCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxExcessiveDeferred"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxDeferred"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxLateCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTotalCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPauseHonored"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxDrop"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxJabber"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxFCSError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxControl"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxFragment"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsLinkDowns"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx1024ToMax"))
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsGroup.setStatus("current")

mtxrPOEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 18)
)
mtxrPOEGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrPOEName"),
        ("MIKROTIK-MIB", "mtxrPOEStatus"),
        ("MIKROTIK-MIB", "mtxrPOEVoltage"),
        ("MIKROTIK-MIB", "mtxrPOECurrent"),
        ("MIKROTIK-MIB", "mtxrPOEPower"))
)
if mibBuilder.loadTexts:
    mtxrPOEGroup.setStatus("current")

mtxrLTEModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 19)
)
mtxrLTEModemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrLTEModemSignalRSSI"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalRSRQ"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalRSRP"),
        ("MIKROTIK-MIB", "mtxrLTEModemCellId"),
        ("MIKROTIK-MIB", "mtxrLTEModemAccessTechnology"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalSINR"),
        ("MIKROTIK-MIB", "mtxrLTEModemEnbId"),
        ("MIKROTIK-MIB", "mtxrLTEModemSectorId"),
        ("MIKROTIK-MIB", "mtxrLTEModemLac"),
        ("MIKROTIK-MIB", "mtxrLTEModemIMEI"),
        ("MIKROTIK-MIB", "mtxrLTEModemIMSI"),
        ("MIKROTIK-MIB", "mtxrLTEModemUICC"),
        ("MIKROTIK-MIB", "mtxrLTEModemRAT"))
)
if mibBuilder.loadTexts:
    mtxrLTEModemGroup.setStatus("current")

mtxrPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 20)
)
mtxrPartitionGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrPartitionName"),
        ("MIKROTIK-MIB", "mtxrPartitionSize"),
        ("MIKROTIK-MIB", "mtxrPartitionVersion"),
        ("MIKROTIK-MIB", "mtxrPartitionActive"),
        ("MIKROTIK-MIB", "mtxrPartitionRunning"))
)
if mibBuilder.loadTexts:
    mtxrPartitionGroup.setStatus("current")

mtxrScriptRunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 21)
)
mtxrScriptRunGroup.setObjects(
    ("MIKROTIK-MIB", "mtxrScriptRunOutput")
)
if mibBuilder.loadTexts:
    mtxrScriptRunGroup.setStatus("current")


# Notification objects

mtxrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0, 1)
)
if mibBuilder.loadTexts:
    mtxrTrap.setStatus(
        "current"
    )

mtxrTemperatureException = NotificationType(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0, 2)
)
if mibBuilder.loadTexts:
    mtxrTemperatureException.setStatus(
        "current"
    )


# Notifications groups

mtxrTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 14)
)
mtxrTrapGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrTrap"),
        ("MIKROTIK-MIB", "mtxrTemperatureException"))
)
if mibBuilder.loadTexts:
    mtxrTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIKROTIK-MIB",
    **{"ObjectIndex": ObjectIndex,
       "HexInt": HexInt,
       "Voltage": Voltage,
       "Temperature": Temperature,
       "Power": Power,
       "GDiv100": GDiv100,
       "GDiv1000": GDiv1000,
       "IDiv1000": IDiv1000,
       "BoolValue": BoolValue,
       "IsakmpCookie": IsakmpCookie,
       "mikrotik": mikrotik,
       "mikrotikExperimentalModule": mikrotikExperimentalModule,
       "mtXRouterOs": mtXRouterOs,
       "mtxrWireless": mtxrWireless,
       "mtxrWlStatTable": mtxrWlStatTable,
       "mtxrWlStatEntry": mtxrWlStatEntry,
       "mtxrWlStatIndex": mtxrWlStatIndex,
       "mtxrWlStatTxRate": mtxrWlStatTxRate,
       "mtxrWlStatRxRate": mtxrWlStatRxRate,
       "mtxrWlStatStrength": mtxrWlStatStrength,
       "mtxrWlStatSsid": mtxrWlStatSsid,
       "mtxrWlStatBssid": mtxrWlStatBssid,
       "mtxrWlStatFreq": mtxrWlStatFreq,
       "mtxrWlStatBand": mtxrWlStatBand,
       "mtxrWlStatTxCCQ": mtxrWlStatTxCCQ,
       "mtxrWlStatRxCCQ": mtxrWlStatRxCCQ,
       "mtxrWlRtabTable": mtxrWlRtabTable,
       "mtxrWlRtabEntry": mtxrWlRtabEntry,
       "mtxrWlRtabAddr": mtxrWlRtabAddr,
       "mtxrWlRtabIface": mtxrWlRtabIface,
       "mtxrWlRtabStrength": mtxrWlRtabStrength,
       "mtxrWlRtabTxBytes": mtxrWlRtabTxBytes,
       "mtxrWlRtabRxBytes": mtxrWlRtabRxBytes,
       "mtxrWlRtabTxPackets": mtxrWlRtabTxPackets,
       "mtxrWlRtabRxPackets": mtxrWlRtabRxPackets,
       "mtxrWlRtabTxRate": mtxrWlRtabTxRate,
       "mtxrWlRtabRxRate": mtxrWlRtabRxRate,
       "mtxrWlRtabRouterOSVersion": mtxrWlRtabRouterOSVersion,
       "mtxrWlRtabUptime": mtxrWlRtabUptime,
       "mtxrWlRtabSignalToNoise": mtxrWlRtabSignalToNoise,
       "mtxrWlRtabTxStrengthCh0": mtxrWlRtabTxStrengthCh0,
       "mtxrWlRtabRxStrengthCh0": mtxrWlRtabRxStrengthCh0,
       "mtxrWlRtabTxStrengthCh1": mtxrWlRtabTxStrengthCh1,
       "mtxrWlRtabRxStrengthCh1": mtxrWlRtabRxStrengthCh1,
       "mtxrWlRtabTxStrengthCh2": mtxrWlRtabTxStrengthCh2,
       "mtxrWlRtabRxStrengthCh2": mtxrWlRtabRxStrengthCh2,
       "mtxrWlRtabTxStrength": mtxrWlRtabTxStrength,
       "mtxrWlRtabRadioName": mtxrWlRtabRadioName,
       "mtxrWlApTable": mtxrWlApTable,
       "mtxrWlApEntry": mtxrWlApEntry,
       "mtxrWlApIndex": mtxrWlApIndex,
       "mtxrWlApTxRate": mtxrWlApTxRate,
       "mtxrWlApRxRate": mtxrWlApRxRate,
       "mtxrWlApSsid": mtxrWlApSsid,
       "mtxrWlApBssid": mtxrWlApBssid,
       "mtxrWlApClientCount": mtxrWlApClientCount,
       "mtxrWlApFreq": mtxrWlApFreq,
       "mtxrWlApBand": mtxrWlApBand,
       "mtxrWlApNoiseFloor": mtxrWlApNoiseFloor,
       "mtxrWlApOverallTxCCQ": mtxrWlApOverallTxCCQ,
       "mtxrWlApAuthClientCount": mtxrWlApAuthClientCount,
       "mtxrWlRtabEntryCount": mtxrWlRtabEntryCount,
       "mtxrWlCMRtabTable": mtxrWlCMRtabTable,
       "mtxrWlCMRtabEntry": mtxrWlCMRtabEntry,
       "mtxrWlCMRtabAddr": mtxrWlCMRtabAddr,
       "mtxrWlCMRtabIface": mtxrWlCMRtabIface,
       "mtxrWlCMRtabUptime": mtxrWlCMRtabUptime,
       "mtxrWlCMRtabTxBytes": mtxrWlCMRtabTxBytes,
       "mtxrWlCMRtabRxBytes": mtxrWlCMRtabRxBytes,
       "mtxrWlCMRtabTxPackets": mtxrWlCMRtabTxPackets,
       "mtxrWlCMRtabRxPackets": mtxrWlCMRtabRxPackets,
       "mtxrWlCMRtabTxRate": mtxrWlCMRtabTxRate,
       "mtxrWlCMRtabRxRate": mtxrWlCMRtabRxRate,
       "mtxrWlCMRtabTxStrength": mtxrWlCMRtabTxStrength,
       "mtxrWlCMRtabRxStrength": mtxrWlCMRtabRxStrength,
       "mtxrWlCMRtabSsid": mtxrWlCMRtabSsid,
       "mtxrWlCMRtabEapIdent": mtxrWlCMRtabEapIdent,
       "mtxrWlCMRtabEntryCount": mtxrWlCMRtabEntryCount,
       "mtxrWlCMTable": mtxrWlCMTable,
       "mtxrWlCMEntry": mtxrWlCMEntry,
       "mtxrWlCMIndex": mtxrWlCMIndex,
       "mtxrWlCMRegClientCount": mtxrWlCMRegClientCount,
       "mtxrWlCMAuthClientCount": mtxrWlCMAuthClientCount,
       "mtxrWlCMState": mtxrWlCMState,
       "mtxrWlCMChannel": mtxrWlCMChannel,
       "mtxrWl60GTable": mtxrWl60GTable,
       "mtxrWl60GEntry": mtxrWl60GEntry,
       "mtxrWl60GIndex": mtxrWl60GIndex,
       "mtxrWl60GMode": mtxrWl60GMode,
       "mtxrWl60GSsid": mtxrWl60GSsid,
       "mtxrWl60GConnected": mtxrWl60GConnected,
       "mtxrWl60GRemote": mtxrWl60GRemote,
       "mtxrWl60GFreq": mtxrWl60GFreq,
       "mtxrWl60GMcs": mtxrWl60GMcs,
       "mtxrWl60GSignal": mtxrWl60GSignal,
       "mtxrWl60GTxSector": mtxrWl60GTxSector,
       "mtxrWl60GTxSectorInfo": mtxrWl60GTxSectorInfo,
       "mtxrWl60GRssi": mtxrWl60GRssi,
       "mtxrWl60GPhyRate": mtxrWl60GPhyRate,
       "mtxrWl60GStaTable": mtxrWl60GStaTable,
       "mtxrWl60GStaEntry": mtxrWl60GStaEntry,
       "mtxrWl60GStaIndex": mtxrWl60GStaIndex,
       "mtxrWl60GStaConnected": mtxrWl60GStaConnected,
       "mtxrWl60GStaRemote": mtxrWl60GStaRemote,
       "mtxrWl60GStaMcs": mtxrWl60GStaMcs,
       "mtxrWl60GStaSignal": mtxrWl60GStaSignal,
       "mtxrWl60GStaTxSector": mtxrWl60GStaTxSector,
       "mtxrWl60GStaPhyRate": mtxrWl60GStaPhyRate,
       "mtxrWl60GStaRssi": mtxrWl60GStaRssi,
       "mtxrWl60GStaDistance": mtxrWl60GStaDistance,
       "mtxrWlCMREntryCount": mtxrWlCMREntryCount,
       "mtxrWlCMRemoteTable": mtxrWlCMRemoteTable,
       "mtxrWlCMRemoteEntry": mtxrWlCMRemoteEntry,
       "mtxrWlCMRemoteIndex": mtxrWlCMRemoteIndex,
       "mtxrWlCMRemoteName": mtxrWlCMRemoteName,
       "mtxrWlCMRemoteState": mtxrWlCMRemoteState,
       "mtxrWlCMRemoteAddress": mtxrWlCMRemoteAddress,
       "mtxrWlCMRemoteRadios": mtxrWlCMRemoteRadios,
       "mtxrQueues": mtxrQueues,
       "mtxrQueueSimpleTable": mtxrQueueSimpleTable,
       "mtxrQueueSimpleEntry": mtxrQueueSimpleEntry,
       "mtxrQueueSimpleIndex": mtxrQueueSimpleIndex,
       "mtxrQueueSimpleName": mtxrQueueSimpleName,
       "mtxrQueueSimpleSrcAddr": mtxrQueueSimpleSrcAddr,
       "mtxrQueueSimpleSrcMask": mtxrQueueSimpleSrcMask,
       "mtxrQueueSimpleDstAddr": mtxrQueueSimpleDstAddr,
       "mtxrQueueSimpleDstMask": mtxrQueueSimpleDstMask,
       "mtxrQueueSimpleIface": mtxrQueueSimpleIface,
       "mtxrQueueSimpleBytesIn": mtxrQueueSimpleBytesIn,
       "mtxrQueueSimpleBytesOut": mtxrQueueSimpleBytesOut,
       "mtxrQueueSimplePacketsIn": mtxrQueueSimplePacketsIn,
       "mtxrQueueSimplePacketsOut": mtxrQueueSimplePacketsOut,
       "mtxrQueueSimplePCQQueuesIn": mtxrQueueSimplePCQQueuesIn,
       "mtxrQueueSimplePCQQueuesOut": mtxrQueueSimplePCQQueuesOut,
       "mtxrQueueSimpleDroppedIn": mtxrQueueSimpleDroppedIn,
       "mtxrQueueSimpleDroppedOut": mtxrQueueSimpleDroppedOut,
       "mtxrQueueTreeTable": mtxrQueueTreeTable,
       "mtxrQueueTreeEntry": mtxrQueueTreeEntry,
       "mtxrQueueTreeIndex": mtxrQueueTreeIndex,
       "mtxrQueueTreeName": mtxrQueueTreeName,
       "mtxrQueueTreeFlow": mtxrQueueTreeFlow,
       "mtxrQueueTreeParentIndex": mtxrQueueTreeParentIndex,
       "mtxrQueueTreeBytes": mtxrQueueTreeBytes,
       "mtxrQueueTreePackets": mtxrQueueTreePackets,
       "mtxrQueueTreeHCBytes": mtxrQueueTreeHCBytes,
       "mtxrQueueTreePCQQueues": mtxrQueueTreePCQQueues,
       "mtxrQueueTreeDropped": mtxrQueueTreeDropped,
       "mtxrHealth": mtxrHealth,
       "mtxrHlCoreVoltage": mtxrHlCoreVoltage,
       "mtxrHlThreeDotThreeVoltage": mtxrHlThreeDotThreeVoltage,
       "mtxrHlFiveVoltage": mtxrHlFiveVoltage,
       "mtxrHlTwelveVoltage": mtxrHlTwelveVoltage,
       "mtxrHlSensorTemperature": mtxrHlSensorTemperature,
       "mtxrHlCpuTemperature": mtxrHlCpuTemperature,
       "mtxrHlBoardTemperature": mtxrHlBoardTemperature,
       "mtxrHlVoltage": mtxrHlVoltage,
       "mtxrHlActiveFan": mtxrHlActiveFan,
       "mtxrHlTemperature": mtxrHlTemperature,
       "mtxrHlProcessorTemperature": mtxrHlProcessorTemperature,
       "mtxrHlPower": mtxrHlPower,
       "mtxrHlCurrent": mtxrHlCurrent,
       "mtxrHlProcessorFrequency": mtxrHlProcessorFrequency,
       "mtxrHlPowerSupplyState": mtxrHlPowerSupplyState,
       "mtxrHlBackupPowerSupplyState": mtxrHlBackupPowerSupplyState,
       "mtxrHlFanSpeed1": mtxrHlFanSpeed1,
       "mtxrHlFanSpeed2": mtxrHlFanSpeed2,
       "mtxrAlarmSocketStatus": mtxrAlarmSocketStatus,
       "mtxrGaugeTable": mtxrGaugeTable,
       "mtxrGaugeTableEntry": mtxrGaugeTableEntry,
       "mtxrGaugeIndex": mtxrGaugeIndex,
       "mtxrGaugeName": mtxrGaugeName,
       "mtxrGaugeValue": mtxrGaugeValue,
       "mtxrGaugeUnit": mtxrGaugeUnit,
       "mtxrLicense": mtxrLicense,
       "mtxrLicSoftwareId": mtxrLicSoftwareId,
       "mtxrLicUpgrUntil": mtxrLicUpgrUntil,
       "mtxrLicLevel": mtxrLicLevel,
       "mtxrLicVersion": mtxrLicVersion,
       "mtxrLicUpgradableTo": mtxrLicUpgradableTo,
       "mtxrHotspot": mtxrHotspot,
       "mtxrHotspotActiveUsersTable": mtxrHotspotActiveUsersTable,
       "mtxrHotspotActiveUsersTableEntry": mtxrHotspotActiveUsersTableEntry,
       "mtxrHotspotActiveUserIndex": mtxrHotspotActiveUserIndex,
       "mtxrHotspotActiveUserServerID": mtxrHotspotActiveUserServerID,
       "mtxrHotspotActiveUserName": mtxrHotspotActiveUserName,
       "mtxrHotspotActiveUserDomain": mtxrHotspotActiveUserDomain,
       "mtxrHotspotActiveUserIP": mtxrHotspotActiveUserIP,
       "mtxrHotspotActiveUserMAC": mtxrHotspotActiveUserMAC,
       "mtxrHotspotActiveUserConnectTime": mtxrHotspotActiveUserConnectTime,
       "mtxrHotspotActiveUserValidTillTime": mtxrHotspotActiveUserValidTillTime,
       "mtxrHotspotActiveUserIdleStartTime": mtxrHotspotActiveUserIdleStartTime,
       "mtxrHotspotActiveUserIdleTimeout": mtxrHotspotActiveUserIdleTimeout,
       "mtxrHotspotActiveUserPingTimeout": mtxrHotspotActiveUserPingTimeout,
       "mtxrHotspotActiveUserBytesIn": mtxrHotspotActiveUserBytesIn,
       "mtxrHotspotActiveUserBytesOut": mtxrHotspotActiveUserBytesOut,
       "mtxrHotspotActiveUserPacketsIn": mtxrHotspotActiveUserPacketsIn,
       "mtxrHotspotActiveUserPacketsOut": mtxrHotspotActiveUserPacketsOut,
       "mtxrHotspotActiveUserLimitBytesIn": mtxrHotspotActiveUserLimitBytesIn,
       "mtxrHotspotActiveUserLimitBytesOut": mtxrHotspotActiveUserLimitBytesOut,
       "mtxrHotspotActiveUserAdvertStatus": mtxrHotspotActiveUserAdvertStatus,
       "mtxrHotspotActiveUserRadius": mtxrHotspotActiveUserRadius,
       "mtxrHotspotActiveUserBlockedByAdvert": mtxrHotspotActiveUserBlockedByAdvert,
       "mtxrDHCP": mtxrDHCP,
       "mtxrDHCPLeaseCount": mtxrDHCPLeaseCount,
       "mtxrSystem": mtxrSystem,
       "mtxrSystemReboot": mtxrSystemReboot,
       "mtxrUSBPowerReset": mtxrUSBPowerReset,
       "mtxrSerialNumber": mtxrSerialNumber,
       "mtxrFirmwareVersion": mtxrFirmwareVersion,
       "mtxrNote": mtxrNote,
       "mtxrBuildTime": mtxrBuildTime,
       "mtxrFirmwareUpgradeVersion": mtxrFirmwareUpgradeVersion,
       "mtxrDisplayName": mtxrDisplayName,
       "mtxrBoardName": mtxrBoardName,
       "mtxrScripts": mtxrScripts,
       "mtxrScriptTable": mtxrScriptTable,
       "mtxrScriptTableEntry": mtxrScriptTableEntry,
       "mtxrScriptIndex": mtxrScriptIndex,
       "mtxrScriptName": mtxrScriptName,
       "mtxrScriptRunCmd": mtxrScriptRunCmd,
       "mtxrTraps": mtxrTraps,
       "mtxrNotifications": mtxrNotifications,
       "mtxrTrap": mtxrTrap,
       "mtxrTemperatureException": mtxrTemperatureException,
       "mtxrNstremeDual": mtxrNstremeDual,
       "mtxrDnStatTable": mtxrDnStatTable,
       "mtxrDnStatEntry": mtxrDnStatEntry,
       "mtxrDnStatIndex": mtxrDnStatIndex,
       "mtxrDnStatTxRate": mtxrDnStatTxRate,
       "mtxrDnStatRxRate": mtxrDnStatRxRate,
       "mtxrDnStatTxStrength": mtxrDnStatTxStrength,
       "mtxrDnStatRxStrength": mtxrDnStatRxStrength,
       "mtxrDnConnected": mtxrDnConnected,
       "mtxrNeighbor": mtxrNeighbor,
       "mtxrNeighborTable": mtxrNeighborTable,
       "mtxrNeighborTableEntry": mtxrNeighborTableEntry,
       "mtxrNeighborIndex": mtxrNeighborIndex,
       "mtxrNeighborIpAddress": mtxrNeighborIpAddress,
       "mtxrNeighborMacAddress": mtxrNeighborMacAddress,
       "mtxrNeighborVersion": mtxrNeighborVersion,
       "mtxrNeighborPlatform": mtxrNeighborPlatform,
       "mtxrNeighborIdentity": mtxrNeighborIdentity,
       "mtxrNeighborSoftwareID": mtxrNeighborSoftwareID,
       "mtxrNeighborInterfaceID": mtxrNeighborInterfaceID,
       "mtxrGps": mtxrGps,
       "mtxrDate": mtxrDate,
       "mtxrLongtitude": mtxrLongtitude,
       "mtxrLatitude": mtxrLatitude,
       "mtxrAltitude": mtxrAltitude,
       "mtxrSpeed": mtxrSpeed,
       "mtxrSattelites": mtxrSattelites,
       "mtxrValid": mtxrValid,
       "mtxrWirelessModem": mtxrWirelessModem,
       "mtxrWirelessModemSignalStrength": mtxrWirelessModemSignalStrength,
       "mtxrWirelessModemSignalECIO": mtxrWirelessModemSignalECIO,
       "mtxrWirelessModemManufacturer": mtxrWirelessModemManufacturer,
       "mtxrWirelessModemModel": mtxrWirelessModemModel,
       "mtxrWirelessModemRevision": mtxrWirelessModemRevision,
       "mtxrWirelessModemIMEI": mtxrWirelessModemIMEI,
       "mtxrWirelessModemIMSI": mtxrWirelessModemIMSI,
       "mtxrWirelessModemAccessTechnology": mtxrWirelessModemAccessTechnology,
       "mtxrWirelessModemFrameErrorRate": mtxrWirelessModemFrameErrorRate,
       "mtxrWirelessModemRSRP": mtxrWirelessModemRSRP,
       "mtxrWirelessModemRSRQ": mtxrWirelessModemRSRQ,
       "mtxrWirelessModemSINR": mtxrWirelessModemSINR,
       "mtxrWirelessModemPinStatus": mtxrWirelessModemPinStatus,
       "mtxrInterfaceStats": mtxrInterfaceStats,
       "mtxrInterfaceStatsTable": mtxrInterfaceStatsTable,
       "mtxrInterfaceStatsEntry": mtxrInterfaceStatsEntry,
       "mtxrInterfaceStatsIndex": mtxrInterfaceStatsIndex,
       "mtxrInterfaceStatsName": mtxrInterfaceStatsName,
       "mtxrInterfaceStatsDriverRxBytes": mtxrInterfaceStatsDriverRxBytes,
       "mtxrInterfaceStatsDriverRxPackets": mtxrInterfaceStatsDriverRxPackets,
       "mtxrInterfaceStatsDriverTxBytes": mtxrInterfaceStatsDriverTxBytes,
       "mtxrInterfaceStatsDriverTxPackets": mtxrInterfaceStatsDriverTxPackets,
       "mtxrInterfaceStatsTxRx64": mtxrInterfaceStatsTxRx64,
       "mtxrInterfaceStatsTxRx65To127": mtxrInterfaceStatsTxRx65To127,
       "mtxrInterfaceStatsTxRx128To255": mtxrInterfaceStatsTxRx128To255,
       "mtxrInterfaceStatsTxRx256To511": mtxrInterfaceStatsTxRx256To511,
       "mtxrInterfaceStatsTxRx512To1023": mtxrInterfaceStatsTxRx512To1023,
       "mtxrInterfaceStatsTxRx1024To1518": mtxrInterfaceStatsTxRx1024To1518,
       "mtxrInterfaceStatsTxRx1519ToMax": mtxrInterfaceStatsTxRx1519ToMax,
       "mtxrInterfaceStatsRxBytes": mtxrInterfaceStatsRxBytes,
       "mtxrInterfaceStatsRxPackets": mtxrInterfaceStatsRxPackets,
       "mtxrInterfaceStatsRxTooShort": mtxrInterfaceStatsRxTooShort,
       "mtxrInterfaceStatsRx64": mtxrInterfaceStatsRx64,
       "mtxrInterfaceStatsRx65To127": mtxrInterfaceStatsRx65To127,
       "mtxrInterfaceStatsRx128To255": mtxrInterfaceStatsRx128To255,
       "mtxrInterfaceStatsRx256To511": mtxrInterfaceStatsRx256To511,
       "mtxrInterfaceStatsRx512To1023": mtxrInterfaceStatsRx512To1023,
       "mtxrInterfaceStatsRx1024To1518": mtxrInterfaceStatsRx1024To1518,
       "mtxrInterfaceStatsRx1519ToMax": mtxrInterfaceStatsRx1519ToMax,
       "mtxrInterfaceStatsRxTooLong": mtxrInterfaceStatsRxTooLong,
       "mtxrInterfaceStatsRxBroadcast": mtxrInterfaceStatsRxBroadcast,
       "mtxrInterfaceStatsRxPause": mtxrInterfaceStatsRxPause,
       "mtxrInterfaceStatsRxMulticast": mtxrInterfaceStatsRxMulticast,
       "mtxrInterfaceStatsRxFCSError": mtxrInterfaceStatsRxFCSError,
       "mtxrInterfaceStatsRxAlignError": mtxrInterfaceStatsRxAlignError,
       "mtxrInterfaceStatsRxFragment": mtxrInterfaceStatsRxFragment,
       "mtxrInterfaceStatsRxOverflow": mtxrInterfaceStatsRxOverflow,
       "mtxrInterfaceStatsRxControl": mtxrInterfaceStatsRxControl,
       "mtxrInterfaceStatsRxUnknownOp": mtxrInterfaceStatsRxUnknownOp,
       "mtxrInterfaceStatsRxLengthError": mtxrInterfaceStatsRxLengthError,
       "mtxrInterfaceStatsRxCodeError": mtxrInterfaceStatsRxCodeError,
       "mtxrInterfaceStatsRxCarrierError": mtxrInterfaceStatsRxCarrierError,
       "mtxrInterfaceStatsRxJabber": mtxrInterfaceStatsRxJabber,
       "mtxrInterfaceStatsRxDrop": mtxrInterfaceStatsRxDrop,
       "mtxrInterfaceStatsTxBytes": mtxrInterfaceStatsTxBytes,
       "mtxrInterfaceStatsTxPackets": mtxrInterfaceStatsTxPackets,
       "mtxrInterfaceStatsTxTooShort": mtxrInterfaceStatsTxTooShort,
       "mtxrInterfaceStatsTx64": mtxrInterfaceStatsTx64,
       "mtxrInterfaceStatsTx65To127": mtxrInterfaceStatsTx65To127,
       "mtxrInterfaceStatsTx128To255": mtxrInterfaceStatsTx128To255,
       "mtxrInterfaceStatsTx256To511": mtxrInterfaceStatsTx256To511,
       "mtxrInterfaceStatsTx512To1023": mtxrInterfaceStatsTx512To1023,
       "mtxrInterfaceStatsTx1024To1518": mtxrInterfaceStatsTx1024To1518,
       "mtxrInterfaceStatsTx1519ToMax": mtxrInterfaceStatsTx1519ToMax,
       "mtxrInterfaceStatsTxTooLong": mtxrInterfaceStatsTxTooLong,
       "mtxrInterfaceStatsTxBroadcast": mtxrInterfaceStatsTxBroadcast,
       "mtxrInterfaceStatsTxPause": mtxrInterfaceStatsTxPause,
       "mtxrInterfaceStatsTxMulticast": mtxrInterfaceStatsTxMulticast,
       "mtxrInterfaceStatsTxUnderrun": mtxrInterfaceStatsTxUnderrun,
       "mtxrInterfaceStatsTxCollision": mtxrInterfaceStatsTxCollision,
       "mtxrInterfaceStatsTxExcessiveCollision": mtxrInterfaceStatsTxExcessiveCollision,
       "mtxrInterfaceStatsTxMultipleCollision": mtxrInterfaceStatsTxMultipleCollision,
       "mtxrInterfaceStatsTxSingleCollision": mtxrInterfaceStatsTxSingleCollision,
       "mtxrInterfaceStatsTxExcessiveDeferred": mtxrInterfaceStatsTxExcessiveDeferred,
       "mtxrInterfaceStatsTxDeferred": mtxrInterfaceStatsTxDeferred,
       "mtxrInterfaceStatsTxLateCollision": mtxrInterfaceStatsTxLateCollision,
       "mtxrInterfaceStatsTxTotalCollision": mtxrInterfaceStatsTxTotalCollision,
       "mtxrInterfaceStatsTxPauseHonored": mtxrInterfaceStatsTxPauseHonored,
       "mtxrInterfaceStatsTxDrop": mtxrInterfaceStatsTxDrop,
       "mtxrInterfaceStatsTxJabber": mtxrInterfaceStatsTxJabber,
       "mtxrInterfaceStatsTxFCSError": mtxrInterfaceStatsTxFCSError,
       "mtxrInterfaceStatsTxControl": mtxrInterfaceStatsTxControl,
       "mtxrInterfaceStatsTxFragment": mtxrInterfaceStatsTxFragment,
       "mtxrInterfaceStatsLinkDowns": mtxrInterfaceStatsLinkDowns,
       "mtxrInterfaceStatsTxRx1024ToMax": mtxrInterfaceStatsTxRx1024ToMax,
       "mtxrPOE": mtxrPOE,
       "mtxrPOETable": mtxrPOETable,
       "mtxrPOEEntry": mtxrPOEEntry,
       "mtxrPOEInterfaceIndex": mtxrPOEInterfaceIndex,
       "mtxrPOEName": mtxrPOEName,
       "mtxrPOEStatus": mtxrPOEStatus,
       "mtxrPOEVoltage": mtxrPOEVoltage,
       "mtxrPOECurrent": mtxrPOECurrent,
       "mtxrPOEPower": mtxrPOEPower,
       "mtxrLTEModem": mtxrLTEModem,
       "mtxrLTEModemTable": mtxrLTEModemTable,
       "mtxrLTEModemEntry": mtxrLTEModemEntry,
       "mtxrLTEModemInterfaceIndex": mtxrLTEModemInterfaceIndex,
       "mtxrLTEModemSignalRSSI": mtxrLTEModemSignalRSSI,
       "mtxrLTEModemSignalRSRQ": mtxrLTEModemSignalRSRQ,
       "mtxrLTEModemSignalRSRP": mtxrLTEModemSignalRSRP,
       "mtxrLTEModemCellId": mtxrLTEModemCellId,
       "mtxrLTEModemAccessTechnology": mtxrLTEModemAccessTechnology,
       "mtxrLTEModemSignalSINR": mtxrLTEModemSignalSINR,
       "mtxrLTEModemEnbId": mtxrLTEModemEnbId,
       "mtxrLTEModemSectorId": mtxrLTEModemSectorId,
       "mtxrLTEModemLac": mtxrLTEModemLac,
       "mtxrLTEModemIMEI": mtxrLTEModemIMEI,
       "mtxrLTEModemIMSI": mtxrLTEModemIMSI,
       "mtxrLTEModemUICC": mtxrLTEModemUICC,
       "mtxrLTEModemRAT": mtxrLTEModemRAT,
       "mtxrPartition": mtxrPartition,
       "mtxrPartitionTable": mtxrPartitionTable,
       "mtxrPartitionEntry": mtxrPartitionEntry,
       "mtxrPartitionIndex": mtxrPartitionIndex,
       "mtxrPartitionName": mtxrPartitionName,
       "mtxrPartitionSize": mtxrPartitionSize,
       "mtxrPartitionVersion": mtxrPartitionVersion,
       "mtxrPartitionActive": mtxrPartitionActive,
       "mtxrPartitionRunning": mtxrPartitionRunning,
       "mtxrScriptRun": mtxrScriptRun,
       "mtxrScriptRunTable": mtxrScriptRunTable,
       "mtxrScriptRunTableEntry": mtxrScriptRunTableEntry,
       "mtxrScriptRunIndex": mtxrScriptRunIndex,
       "mtxrScriptRunOutput": mtxrScriptRunOutput,
       "mtxrOptical": mtxrOptical,
       "mtxrOpticalTable": mtxrOpticalTable,
       "mtxrOpticalTableEntry": mtxrOpticalTableEntry,
       "mtxrOpticalIndex": mtxrOpticalIndex,
       "mtxrOpticalName": mtxrOpticalName,
       "mtxrOpticalRxLoss": mtxrOpticalRxLoss,
       "mtxrOpticalTxFault": mtxrOpticalTxFault,
       "mtxrOpticalWavelength": mtxrOpticalWavelength,
       "mtxrOpticalTemperature": mtxrOpticalTemperature,
       "mtxrOpticalSupplyVoltage": mtxrOpticalSupplyVoltage,
       "mtxrOpticalTxBiasCurrent": mtxrOpticalTxBiasCurrent,
       "mtxrOpticalTxPower": mtxrOpticalTxPower,
       "mtxrOpticalRxPower": mtxrOpticalRxPower,
       "mtxrOpticalVendorName": mtxrOpticalVendorName,
       "mtxrOpticalVendorSerial": mtxrOpticalVendorSerial,
       "mtxrIPSec": mtxrIPSec,
       "mtxrIkeSACount": mtxrIkeSACount,
       "mtxrIkeSATable": mtxrIkeSATable,
       "mtxrIkeSATableEntry": mtxrIkeSATableEntry,
       "mtxrIkeSAIndex": mtxrIkeSAIndex,
       "mtxrIkeSAInitiatorCookie": mtxrIkeSAInitiatorCookie,
       "mtxrIkeSAResponderCookie": mtxrIkeSAResponderCookie,
       "mtxrIkeSAResponder": mtxrIkeSAResponder,
       "mtxrIkeSANatt": mtxrIkeSANatt,
       "mtxrIkeSAVersion": mtxrIkeSAVersion,
       "mtxrIkeSAState": mtxrIkeSAState,
       "mtxrIkeSAUptime": mtxrIkeSAUptime,
       "mtxrIkeSASeen": mtxrIkeSASeen,
       "mtxrIkeSAIdentity": mtxrIkeSAIdentity,
       "mtxrIkeSAPh2Count": mtxrIkeSAPh2Count,
       "mtxrIkeSALocalAddressType": mtxrIkeSALocalAddressType,
       "mtxrIkeSALocalAddress": mtxrIkeSALocalAddress,
       "mtxrIkeSALocalPort": mtxrIkeSALocalPort,
       "mtxrIkeSAPeerAddressType": mtxrIkeSAPeerAddressType,
       "mtxrIkeSAPeerAddress": mtxrIkeSAPeerAddress,
       "mtxrIkeSAPeerPort": mtxrIkeSAPeerPort,
       "mtxrIkeSADynamicAddressType": mtxrIkeSADynamicAddressType,
       "mtxrIkeSADynamicAddress": mtxrIkeSADynamicAddress,
       "mtxrIkeSATxBytes": mtxrIkeSATxBytes,
       "mtxrIkeSARxBytes": mtxrIkeSARxBytes,
       "mtxrIkeSATxPackets": mtxrIkeSATxPackets,
       "mtxrIkeSARxPackets": mtxrIkeSARxPackets,
       "mtxrWifi": mtxrWifi,
       "mtxrWifiCapsman": mtxrWifiCapsman,
       "mtxrWifiCapsmanEnabled": mtxrWifiCapsmanEnabled,
       "mtxrWifiCapsmanInterfaces": mtxrWifiCapsmanInterfaces,
       "mtxrWifiCapsmanCACertificate": mtxrWifiCapsmanCACertificate,
       "mtxrWifiCapsmanCertificate": mtxrWifiCapsmanCertificate,
       "mtxrWifiCapsmanRequirePeerCertificate": mtxrWifiCapsmanRequirePeerCertificate,
       "mtxrWifiCapsmanPackagePath": mtxrWifiCapsmanPackagePath,
       "mtxrWifiCapsmanUpgradePolicy": mtxrWifiCapsmanUpgradePolicy,
       "mtxrWifiCapsmanGeneratedCaCertificate": mtxrWifiCapsmanGeneratedCaCertificate,
       "mtxrWifiCapsmanGeneratedCertificate": mtxrWifiCapsmanGeneratedCertificate,
       "mtxrWifiCap": mtxrWifiCap,
       "mtxrCapEnabled": mtxrCapEnabled,
       "mtxrCapInterfaces": mtxrCapInterfaces,
       "mtxrCapCertificate": mtxrCapCertificate,
       "mtxrCapCapsManAddresses": mtxrCapCapsManAddresses,
       "mtxrCapCapsManNames": mtxrCapCapsManNames,
       "mtxrCapCapsManCertificateCommonNames": mtxrCapCapsManCertificateCommonNames,
       "mtxrCapLockToCapsMan": mtxrCapLockToCapsMan,
       "mtxrCapSlavesStatic": mtxrCapSlavesStatic,
       "mtxrCapSlavesDatapath": mtxrCapSlavesDatapath,
       "mtxrCapRequestedCertificate": mtxrCapRequestedCertificate,
       "mtxrCapLockedCapsManCommonName": mtxrCapLockedCapsManCommonName,
       "mtxrCapCurrentCapsManAddress": mtxrCapCurrentCapsManAddress,
       "mtxrCapCurrentCapsManIdentity": mtxrCapCurrentCapsManIdentity,
       "mtxrRemoteCapTable": mtxrRemoteCapTable,
       "mtxrWifiRemoteCapEntry": mtxrWifiRemoteCapEntry,
       "mtxrRemoteCapId": mtxrRemoteCapId,
       "mtxrRemoteCapAddress": mtxrRemoteCapAddress,
       "mtxrRemoteCapIdentity": mtxrRemoteCapIdentity,
       "mtxrRemoteCapBoardName": mtxrRemoteCapBoardName,
       "mtxrRemoteCapSerial": mtxrRemoteCapSerial,
       "mtxrRemoteCapVersion": mtxrRemoteCapVersion,
       "mtxrRemoteCapBaseMac": mtxrRemoteCapBaseMac,
       "mtxrRemoteCapCommonName": mtxrRemoteCapCommonName,
       "mtxrRemoteCapState": mtxrRemoteCapState,
       "mtxrWifiRegistrationTable": mtxrWifiRegistrationTable,
       "mtxrWifiRegistrationTableEntry": mtxrWifiRegistrationTableEntry,
       "mtxrWifiRegistrationMacAddress": mtxrWifiRegistrationMacAddress,
       "mtxrWifiRegistrationInterface": mtxrWifiRegistrationInterface,
       "mtxrWifiRegistrationSsid": mtxrWifiRegistrationSsid,
       "mtxrWifiRegistrationUptime": mtxrWifiRegistrationUptime,
       "mtxrWifiRegistrationLastActivity": mtxrWifiRegistrationLastActivity,
       "mtxrWifiRegistrationSignal": mtxrWifiRegistrationSignal,
       "mtxrWifiRegistrationAuthType": mtxrWifiRegistrationAuthType,
       "mtxrWifiRegistrationBand": mtxrWifiRegistrationBand,
       "mtxrWifiRegistrationTxRate": mtxrWifiRegistrationTxRate,
       "mtxrWifiRegistrationRxRate": mtxrWifiRegistrationRxRate,
       "mtxrWifiRegistrationTxPackets": mtxrWifiRegistrationTxPackets,
       "mtxrWifiRegistrationRxPackets": mtxrWifiRegistrationRxPackets,
       "mtxrWifiRegistrationTxBytes": mtxrWifiRegistrationTxBytes,
       "mtxrWifiRegistrationRxBytes": mtxrWifiRegistrationRxBytes,
       "mtxrWifiRegistrationTxBitsPerSecond": mtxrWifiRegistrationTxBitsPerSecond,
       "mtxrWifiRegistrationRxBitsPerSecond": mtxrWifiRegistrationRxBitsPerSecond,
       "mtxrWifiRegistrationVlanId": mtxrWifiRegistrationVlanId,
       "mtxrWifiRegistrationAuthorized": mtxrWifiRegistrationAuthorized,
       "mtxrWifiInterfaces": mtxrWifiInterfaces,
       "mtxrWifiInterfacesEntry": mtxrWifiInterfacesEntry,
       "mtxrWifiInterfacesId": mtxrWifiInterfacesId,
       "mtxrWifiInterfacesName": mtxrWifiInterfacesName,
       "mtxrWifiInterfacesSsid": mtxrWifiInterfacesSsid,
       "mtxrWifiInterfacesFreq": mtxrWifiInterfacesFreq,
       "mtxrCT": mtxrCT,
       "mtxrCtStatsGroup": mtxrCtStatsGroup,
       "mtxrCtTotalEntries": mtxrCtTotalEntries,
       "mtxrCtIP4Entries": mtxrCtIP4Entries,
       "mtxrCtIP6Entries": mtxrCtIP6Entries,
       "mtXMetaInfo": mtXMetaInfo,
       "mtXRouterOsGroups": mtXRouterOsGroups,
       "mtxrWirelessGroup": mtxrWirelessGroup,
       "mtxrQueueGroup": mtxrQueueGroup,
       "mtxrHealthGroup": mtxrHealthGroup,
       "mtxrLincenseGroup": mtxrLincenseGroup,
       "mtxrHotspotActiveUserGroup": mtxrHotspotActiveUserGroup,
       "mtxrOpticalGroup": mtxrOpticalGroup,
       "mtxrIkeSAGroup": mtxrIkeSAGroup,
       "mtxrScriptGroup": mtxrScriptGroup,
       "mtxrNstremeDualGroup": mtxrNstremeDualGroup,
       "mtxrNeighborGroup": mtxrNeighborGroup,
       "mtxrDHCPGroup": mtxrDHCPGroup,
       "mtxrSystemGroup": mtxrSystemGroup,
       "mtxrTrapGroup": mtxrTrapGroup,
       "mtxrGPSGroup": mtxrGPSGroup,
       "mtxrWirelessModemGroup": mtxrWirelessModemGroup,
       "mtxrInterfaceStatsGroup": mtxrInterfaceStatsGroup,
       "mtxrPOEGroup": mtxrPOEGroup,
       "mtxrLTEModemGroup": mtxrLTEModemGroup,
       "mtxrPartitionGroup": mtxrPartitionGroup,
       "mtxrScriptRunGroup": mtxrScriptRunGroup}
)
