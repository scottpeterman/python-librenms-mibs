# SNMP MIB module (TELESTE-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teleste\TELESTE-ROOT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:03 2025
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



class TDisplayString(OctetString):
    """Custom type TDisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class TPhysAddress(OctetString):
    """Custom type TPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class Int8(Integer32):
    """Custom type Int8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )





class Int16(Integer32):
    """Custom type Int16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32768),
    )





class Uint8(Integer32):
    """Custom type Uint8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Uint16(Integer32):
    """Custom type Uint16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )





class Uint32(Integer32):
    """Custom type Uint32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class DateAndTime(DisplayString):
    """Custom type DateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 28),
    )





class ValueStatus(Integer32):
    """Custom type ValueStatus based on Integer32"""
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
        *(("valueNormal", 1),
          ("valueHIHI", 2),
          ("valueHi", 3),
          ("valueLo", 4),
          ("valueLOLO", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Teleste_ObjectIdentity = ObjectIdentity
teleste = _Teleste_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715)
)
_Ems_ObjectIdentity = ObjectIdentity
ems = _Ems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 1)
)
_Gendata_ObjectIdentity = ObjectIdentity
gendata = _Gendata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 2)
)
_Bk_ObjectIdentity = ObjectIdentity
bk = _Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 3)
)
_Bxx_ObjectIdentity = ObjectIdentity
bxx = _Bxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 4)
)
_Dvo_ObjectIdentity = ObjectIdentity
dvo = _Dvo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 5)
)
_Dvx_ObjectIdentity = ObjectIdentity
dvx = _Dvx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 6)
)
_Inf_ObjectIdentity = ObjectIdentity
inf = _Inf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 7)
)
_Atmux_ObjectIdentity = ObjectIdentity
atmux = _Atmux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 8)
)
_Easi_ObjectIdentity = ObjectIdentity
easi = _Easi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 9)
)
_Emt_ObjectIdentity = ObjectIdentity
emt = _Emt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 10)
)
_Acx_ObjectIdentity = ObjectIdentity
acx = _Acx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 11)
)
_Etth_ObjectIdentity = ObjectIdentity
etth = _Etth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 12)
)
_Hdo_ObjectIdentity = ObjectIdentity
hdo = _Hdo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 14)
)
_Cfo_ObjectIdentity = ObjectIdentity
cfo = _Cfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 15)
)
_Ftth_ObjectIdentity = ObjectIdentity
ftth = _Ftth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 16)
)
_Luminato_ObjectIdentity = ObjectIdentity
luminato = _Luminato_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99)
)
_Functional_ObjectIdentity = ObjectIdentity
functional = _Functional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100)
)
_HmsModem_ObjectIdentity = ObjectIdentity
hmsModem = _HmsModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 1)
)
_SpectrumAnalyser_ObjectIdentity = ObjectIdentity
spectrumAnalyser = _SpectrumAnalyser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 2)
)
_PilotGenerator_ObjectIdentity = ObjectIdentity
pilotGenerator = _PilotGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 3)
)
_Ntpcontrol_ObjectIdentity = ObjectIdentity
ntpcontrol = _Ntpcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 4)
)
_HfcOptics_ObjectIdentity = ObjectIdentity
hfcOptics = _HfcOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 10)
)
_HeadEnd_ObjectIdentity = ObjectIdentity
headEnd = _HeadEnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 100, 20)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 999)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELESTE-ROOT-MIB",
    **{"TDisplayString": TDisplayString,
       "TPhysAddress": TPhysAddress,
       "Int8": Int8,
       "Int16": Int16,
       "Uint8": Uint8,
       "Uint16": Uint16,
       "Uint32": Uint32,
       "DateAndTime": DateAndTime,
       "ValueStatus": ValueStatus,
       "teleste": teleste,
       "ems": ems,
       "gendata": gendata,
       "bk": bk,
       "bxx": bxx,
       "dvo": dvo,
       "dvx": dvx,
       "inf": inf,
       "atmux": atmux,
       "easi": easi,
       "emt": emt,
       "acx": acx,
       "etth": etth,
       "hdo": hdo,
       "cfo": cfo,
       "ftth": ftth,
       "luminato": luminato,
       "common": common,
       "functional": functional,
       "hmsModem": hmsModem,
       "spectrumAnalyser": spectrumAnalyser,
       "pilotGenerator": pilotGenerator,
       "ntpcontrol": ntpcontrol,
       "hfcOptics": hfcOptics,
       "headEnd": headEnd,
       "experimental": experimental}
)
