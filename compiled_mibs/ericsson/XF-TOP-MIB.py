# SNMP MIB module (XF-TOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-TOP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:46 2025
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

miniLinkXF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81)
)
if mibBuilder.loadTexts:
    miniLinkXF.setRevisions(
        ("2012-10-10 16:00",
         "2012-08-31 16:00",
         "2012-06-13 16:00",
         "2011-09-10 12:00",
         "2010-09-22 11:00",
         "2010-04-20 10:00",
         "2010-01-26 10:00",
         "2009-03-16 12:00",
         "2009-01-22 11:00",
         "2008-02-25 14:44",
         "2006-01-26 12:24",
         "2005-02-25 16:00",
         "2004-01-23 11:11",
         "2003-06-19 09:24",
         "2002-03-07 13:29",
         "2001-10-08 15:01",
         "2001-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class XfProductnumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "30t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class XfProductRevision(TextualConvention, OctetString):
    status = "current"
    displayHint = "40t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class Xf24HrsSeconds(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )



class Xf15MinSeconds(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )



class Xf24HrsSecondsGauge(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class Xf15MinSecondsGauge(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )



# MIB Managed Objects in the order of their OIDs

_Ericsson_ObjectIdentity = ObjectIdentity
ericsson = _Ericsson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193)
)
_XfSysId_ObjectIdentity = ObjectIdentity
xfSysId = _XfSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 1)
)
_XfPlatform_ObjectIdentity = ObjectIdentity
xfPlatform = _XfPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2)
)
_XfMediaSpecific_ObjectIdentity = ObjectIdentity
xfMediaSpecific = _XfMediaSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3)
)
_XfPDH_ObjectIdentity = ObjectIdentity
xfPDH = _XfPDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 1)
)
_XfSDH_ObjectIdentity = ObjectIdentity
xfSDH = _XfSDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 2)
)
_XfMCR_ObjectIdentity = ObjectIdentity
xfMCR = _XfMCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 3)
)
_XfRadioLink_ObjectIdentity = ObjectIdentity
xfRadioLink = _XfRadioLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4)
)
_XfServiceApplications_ObjectIdentity = ObjectIdentity
xfServiceApplications = _XfServiceApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4)
)
_XfEthernetBridge_ObjectIdentity = ObjectIdentity
xfEthernetBridge = _XfEthernetBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4, 1)
)
_XfAtmAggregationUnit_ObjectIdentity = ObjectIdentity
xfAtmAggregationUnit = _XfAtmAggregationUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4, 2)
)
_XfSdhAdm_ObjectIdentity = ObjectIdentity
xfSdhAdm = _XfSdhAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4, 3)
)
_XfCesService_ObjectIdentity = ObjectIdentity
xfCesService = _XfCesService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4, 4)
)
_XfRps_ObjectIdentity = ObjectIdentity
xfRps = _XfRps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 4, 5)
)
_XfIpSau_ObjectIdentity = ObjectIdentity
xfIpSau = _XfIpSau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 5)
)
_XfCN210_ObjectIdentity = ObjectIdentity
xfCN210 = _XfCN210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 6)
)
_XfCN500_ObjectIdentity = ObjectIdentity
xfCN500 = _XfCN500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 7)
)
_XfPT6010_ObjectIdentity = ObjectIdentity
xfPT6010 = _XfPT6010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-TOP-MIB",
    **{"XfProductnumber": XfProductnumber,
       "XfProductRevision": XfProductRevision,
       "Xf24HrsSeconds": Xf24HrsSeconds,
       "Xf15MinSeconds": Xf15MinSeconds,
       "Xf24HrsSecondsGauge": Xf24HrsSecondsGauge,
       "Xf15MinSecondsGauge": Xf15MinSecondsGauge,
       "ericsson": ericsson,
       "miniLinkXF": miniLinkXF,
       "xfSysId": xfSysId,
       "xfPlatform": xfPlatform,
       "xfMediaSpecific": xfMediaSpecific,
       "xfPDH": xfPDH,
       "xfSDH": xfSDH,
       "xfMCR": xfMCR,
       "xfRadioLink": xfRadioLink,
       "xfServiceApplications": xfServiceApplications,
       "xfEthernetBridge": xfEthernetBridge,
       "xfAtmAggregationUnit": xfAtmAggregationUnit,
       "xfSdhAdm": xfSdhAdm,
       "xfCesService": xfCesService,
       "xfRps": xfRps,
       "xfIpSau": xfIpSau,
       "xfCN210": xfCN210,
       "xfCN500": xfCN500,
       "xfPT6010": xfPT6010}
)
