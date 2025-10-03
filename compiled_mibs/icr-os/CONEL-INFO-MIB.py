# SNMP MIB module (CONEL-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icr-os\CONEL-INFO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:11 2025
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
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 6)
)
_InfoProduct_Type = OctetString
_InfoProduct_Object = MibScalar
infoProduct = _InfoProduct_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 1),
    _InfoProduct_Type()
)
infoProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProduct.setStatus("current")
_InfoFirmware_Type = OctetString
_InfoFirmware_Object = MibScalar
infoFirmware = _InfoFirmware_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 2),
    _InfoFirmware_Type()
)
infoFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFirmware.setStatus("current")
_InfoSN_Type = OctetString
_InfoSN_Object = MibScalar
infoSN = _InfoSN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 3),
    _InfoSN_Type()
)
infoSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSN.setStatus("current")
_InfoIMEI_Type = OctetString
_InfoIMEI_Object = MibScalar
infoIMEI = _InfoIMEI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 4),
    _InfoIMEI_Type()
)
infoIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIMEI.setStatus("current")
_InfoESN_Type = OctetString
_InfoESN_Object = MibScalar
infoESN = _InfoESN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 5),
    _InfoESN_Type()
)
infoESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoESN.setStatus("current")
_InfoMEID_Type = OctetString
_InfoMEID_Object = MibScalar
infoMEID = _InfoMEID_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 6),
    _InfoMEID_Type()
)
infoMEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMEID.setStatus("current")
_InfoICCID_Type = OctetString
_InfoICCID_Object = MibScalar
infoICCID = _InfoICCID_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 7),
    _InfoICCID_Type()
)
infoICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoICCID.setStatus("current")
_InfoIMSI_Type = OctetString
_InfoIMSI_Object = MibScalar
infoIMSI = _InfoIMSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 8),
    _InfoIMSI_Type()
)
infoIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIMSI.setStatus("current")
_Info2IMEI_Type = OctetString
_Info2IMEI_Object = MibScalar
info2IMEI = _Info2IMEI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 104),
    _Info2IMEI_Type()
)
info2IMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info2IMEI.setStatus("current")
_Info2ESN_Type = OctetString
_Info2ESN_Object = MibScalar
info2ESN = _Info2ESN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 105),
    _Info2ESN_Type()
)
info2ESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info2ESN.setStatus("current")
_Info2MEID_Type = OctetString
_Info2MEID_Object = MibScalar
info2MEID = _Info2MEID_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 106),
    _Info2MEID_Type()
)
info2MEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info2MEID.setStatus("current")
_Info2ICCID_Type = OctetString
_Info2ICCID_Object = MibScalar
info2ICCID = _Info2ICCID_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 107),
    _Info2ICCID_Type()
)
info2ICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info2ICCID.setStatus("current")
_Info2IMSI_Type = OctetString
_Info2IMSI_Object = MibScalar
info2IMSI = _Info2IMSI_Object(
    (1, 3, 6, 1, 4, 1, 30140, 6, 108),
    _Info2IMSI_Type()
)
info2IMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info2IMSI.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-INFO-MIB",
    **{"conel": conel,
       "info": info,
       "infoProduct": infoProduct,
       "infoFirmware": infoFirmware,
       "infoSN": infoSN,
       "infoIMEI": infoIMEI,
       "infoESN": infoESN,
       "infoMEID": infoMEID,
       "infoICCID": infoICCID,
       "infoIMSI": infoIMSI,
       "info2IMEI": info2IMEI,
       "info2ESN": info2ESN,
       "info2MEID": info2MEID,
       "info2ICCID": info2ICCID,
       "info2IMSI": info2IMSI}
)
