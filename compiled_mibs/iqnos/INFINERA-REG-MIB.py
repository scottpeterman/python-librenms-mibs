# SNMP MIB module (INFINERA-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\iqnos\INFINERA-REG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:06 2025
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

(iso,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "iso")

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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

infinera = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296)
)
if mibBuilder.loadTexts:
    infinera.setRevisions(
        ("2008-09-05 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Std_ObjectIdentity = ObjectIdentity
std = _Std_ObjectIdentity(
    (1, 0)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Don_ObjectIdentity = ObjectIdentity
don = _Don_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2)
)
if mibBuilder.loadTexts:
    don.setStatus("current")
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 1)
)
if mibBuilder.loadTexts:
    base.setStatus("current")
_Ne_ObjectIdentity = ObjectIdentity
ne = _Ne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2)
)
if mibBuilder.loadTexts:
    ne.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1)
)
_InfnNE_ObjectIdentity = ObjectIdentity
infnNE = _InfnNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8)
)
_CommonEquipment_ObjectIdentity = ObjectIdentity
commonEquipment = _CommonEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9)
)
_CommonTerminationPoint_ObjectIdentity = ObjectIdentity
commonTerminationPoint = _CommonTerminationPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10)
)
_CommonPerfMon_ObjectIdentity = ObjectIdentity
commonPerfMon = _CommonPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11)
)
_CommonProfile_ObjectIdentity = ObjectIdentity
commonProfile = _CommonProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 12)
)
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 13)
)
_NtpServer_ObjectIdentity = ObjectIdentity
ntpServer = _NtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 14)
)
_FeatureX_ObjectIdentity = ObjectIdentity
featureX = _FeatureX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 15)
)
_Dtn_ObjectIdentity = ObjectIdentity
dtn = _Dtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2)
)
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1)
)
_TerminationPoint_ObjectIdentity = ObjectIdentity
terminationPoint = _TerminationPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2)
)
_PerfMon_ObjectIdentity = ObjectIdentity
perfMon = _PerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3)
)
_PxmOthers_ObjectIdentity = ObjectIdentity
pxmOthers = _PxmOthers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 4)
)
_Ola_ObjectIdentity = ObjectIdentity
ola = _Ola_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4)
)
_Macsec_ObjectIdentity = ObjectIdentity
macsec = _Macsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 1)
)
_MacsecTP_ObjectIdentity = ObjectIdentity
macsecTP = _MacsecTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 1, 2)
)
_MacsecPerfMon_ObjectIdentity = ObjectIdentity
macsecPerfMon = _MacsecPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 1, 3)
)
_Ike_ObjectIdentity = ObjectIdentity
ike = _Ike_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 2)
)
_Acf_ObjectIdentity = ObjectIdentity
acf = _Acf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 3)
)
_SignedImages_ObjectIdentity = ObjectIdentity
signedImages = _SignedImages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 4, 5)
)
_Cert_ObjectIdentity = ObjectIdentity
cert = _Cert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 5)
)
_Ems_ObjectIdentity = ObjectIdentity
ems = _Ems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3)
)
if mibBuilder.loadTexts:
    ems.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-REG-MIB",
    **{"std": std,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "infinera": infinera,
       "don": don,
       "base": base,
       "ne": ne,
       "common": common,
       "infnNE": infnNE,
       "commonEquipment": commonEquipment,
       "commonTerminationPoint": commonTerminationPoint,
       "commonPerfMon": commonPerfMon,
       "commonProfile": commonProfile,
       "syslog": syslog,
       "ntpServer": ntpServer,
       "featureX": featureX,
       "dtn": dtn,
       "equipment": equipment,
       "terminationPoint": terminationPoint,
       "perfMon": perfMon,
       "pxmOthers": pxmOthers,
       "ola": ola,
       "security": security,
       "macsec": macsec,
       "macsecTP": macsecTP,
       "macsecPerfMon": macsecPerfMon,
       "ike": ike,
       "acf": acf,
       "signedImages": signedImages,
       "cert": cert,
       "ems": ems}
)
