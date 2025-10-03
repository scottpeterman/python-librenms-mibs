# SNMP MIB module (NWAYSMSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\NWAYSMSS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:06 2025
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

(Integer32,) = mibBuilder.importSymbols(
    "SNMPv2-SMI-v1",
    "Integer32")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AtmPrivateAddrEsi(OctetString):
    """Custom type AtmPrivateAddrEsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class AtmSelector(OctetString):
    """Custom type AtmSelector based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1





class AtmVccTrafficType(Integer32):
    """Custom type AtmVccTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("reservedBandwidth", 2))
    )





class Bandwidth(Integer32):
    """Custom type Bandwidth based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NwaysMSS_ObjectIdentity = ObjectIdentity
nwaysMSS = _NwaysMSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118)
)
_MssCommon_ObjectIdentity = ObjectIdentity
mssCommon = _MssCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1)
)
_MssCommonHWVPD_ObjectIdentity = ObjectIdentity
mssCommonHWVPD = _MssCommonHWVPD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 1)
)
_MssCmnSrvrs_ObjectIdentity = ObjectIdentity
mssCmnSrvrs = _MssCmnSrvrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2)
)
_MssServerLanE_ObjectIdentity = ObjectIdentity
mssServerLanE = _MssServerLanE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1)
)
_MssCmnClnts_ObjectIdentity = ObjectIdentity
mssCmnClnts = _MssCmnClnts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NWAYSMSS-MIB",
    **{"AtmPrivateAddrEsi": AtmPrivateAddrEsi,
       "AtmSelector": AtmSelector,
       "AtmVccTrafficType": AtmVccTrafficType,
       "Bandwidth": Bandwidth,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "nwaysMSS": nwaysMSS,
       "mssCommon": mssCommon,
       "mssCommonHWVPD": mssCommonHWVPD,
       "mssCmnSrvrs": mssCmnSrvrs,
       "mssServerLanE": mssServerLanE,
       "mssCmnClnts": mssCmnClnts}
)
